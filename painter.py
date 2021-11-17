
import time
# from pyclick import HumanClicker
import pyautogui
import os
import pyperclip
import PIL
from datetime import datetime  
import sys

from ma_calibration import x_coord, y_coord, color_coord, neutral_coord, edit_coord, submit_coord, ok_coord


def setup() :
    global neutral_coord
    global edit_coord

    pyautogui.moveTo(neutral_coord)
    pyautogui.click()
    time.sleep(1)
    pyautogui.press('f5')
    time.sleep(10)
    pyautogui.moveTo(edit_coord)
    pyautogui.click()
    time.sleep(10)
    pyautogui.moveTo(neutral_coord)
    time.sleep(1)
    pyautogui.scroll(-1)
    time.sleep(1)
    pyautogui.scroll(-1)
    time.sleep(2)
        
def get_pixel_color(x, y) :
    global x_coord
    global y_coord
    global color_coord
    pyautogui.moveTo(x_coord)
    pyautogui.click()
    for _ in range(5) :
        pyautogui.press('right')
    for _ in range(5) :
        pyautogui.press('backspace')
    pyautogui.typewrite(str(x), interval=0.1)

    pyautogui.moveTo(y_coord)
    pyautogui.click()
    for _ in range(5) :
        pyautogui.press('right')
    for _ in range(5) :
        pyautogui.press('backspace')
    pyautogui.typewrite(str(y) + "\n", interval=0.1)

    pyautogui.moveTo(color_coord)
    pyautogui.click()
    pyautogui.hotkey('ctrl', 'q')
    pyautogui.keyDown('ctrl')
    pyautogui.press('c')
    pyautogui.keyUp('ctrl')

    value = pyperclip.paste()[1:]
    return value.lower()

def set_pixel_color(x, y, color) :
    global x_coord
    global y_coord
    global color_coord
    global submit_coord
    global ok_coord

    pyautogui.moveTo(x_coord)
    pyautogui.click()
    for _ in range(5) :
        pyautogui.press('right')
    for _ in range(5) :
        pyautogui.press('backspace')
    pyautogui.typewrite(str(x), interval=0.1)

    pyautogui.moveTo(y_coord)
    pyautogui.click()
    for _ in range(5) :
        pyautogui.press('right')
    for _ in range(5) :
        pyautogui.press('backspace')
    pyautogui.typewrite(str(y), interval=0.1)

    pyautogui.moveTo(color_coord)
    pyautogui.click()
    for _ in range(7) :
        pyautogui.press('right')
    for _ in range(7) :
        pyautogui.press('backspace')
    pyautogui.typewrite('#' + color, interval=0.1)
    pyautogui.moveTo(submit_coord)
    pyautogui.click()
    time.sleep(3)
    pyautogui.moveTo(ok_coord)
    pyautogui.click()


def rgba2hex(pixel) :
    r, g, b, _ = pixel
    return '{:02x}{:02x}{:02x}'.format(r, g, b)



def main() :
    # offset_x = 224
    # offset_y = 72
    # tardis = PIL.Image.open('tardis.png')


    offset_x = 1
    offset_y = 186
    tardis = PIL.Image.open('rickroll.png')

    width, height = tardis.size
    last_update = 0


    while True :
        for i in range(height) :
            for j in range(width) :
                while time.time() - last_update < 118 :
                    pass
                if get_pixel_color(offset_x + j, offset_y + i) != rgba2hex(tardis.getpixel((j, i))):
                    ct = datetime.now()
                    print(j, i, offset_x + j, offset_y + i, rgba2hex(tardis.getpixel((j, i))), f"{ct.hour}:{ct.minute}:{ct.second}", end='\n\n')
                    set_pixel_color(offset_x + j, offset_y + i, rgba2hex(tardis.getpixel((j, i))))
                    last_update = time.time()
                    setup()

if __name__ == '__main__' :
    setup()
    main()
            
    