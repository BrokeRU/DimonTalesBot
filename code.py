from PIL import ImageGrab
import os
import time
import win32api, win32con
import win32com.client
from PIL import ImageOps
from numpy import *

shell = win32com.client.Dispatch("WScript.Shell")

x_pad = 365
y_pad = 188

current_line = 1


def screenGrab():
	box = (x_pad+1, y_pad+1, x_pad+805, y_pad+530)
	# box = (336, 189, 1161, 719)
	im = ImageGrab.grab(box)
	# im.save(os.getcwd() + '\\snap__' + str(int(time.time())) + '.png', 'PNG')
	rgb_im = im.convert('RGB')
	return rgb_im

def mousePos(cord):
	win32api.SetCursorPos((x_pad + cord[0], y_pad + cord[1]))


def leftClick():
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
	time.sleep(.1)
	win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
	print("Click.")


def startGame():
	mousePos((296, 474))
	leftClick()


def check_duck(line):
	global current_line
	im = screenGrab()
	if im.getpixel((10, 10)) == (0, 0, 0):
		print("Finish.")
		exit()
	if line == 1:
		for x in range(465, 745, 25):
			# print(im.getpixel((145, 269)));
			if im.getpixel((x, 269)) == (255, 225, 48):
				print("DOWN")
				shell.SendKeys("{DOWN}")
				current_line = 0
				break
	elif line == 0:
		for x in range(465, 745, 25):
			if im.getpixel((x, 439)) == (255, 225, 48):
				print("UP")
				shell.SendKeys("{UP}")
				current_line = 1
				break
	else:
		print("Incorrect line!");


def main():
	startGame()
	start_time = time.time()
	while True:
		check_duck(current_line)
		if time.time() - starttime > 15:
			time.sleep(.025)
		else:
			time.sleep(.65)


if __name__ == '__main__':
	main()