from PIL import ImageGrab
import os
import time

x_pad = 335
y_pad = 188

def screenGrab():
    box = (x_pad+1, y_pad+1, x_pad+825, y_pad+530)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\snap__' + str(int(time.time())) + '.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()