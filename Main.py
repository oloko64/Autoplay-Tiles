import time
import pyautogui
from PIL import Image
from mss import mss
##
##

# This is the website that I am playing the game: https://www.silvergames.com/en/piano-tiles#play

##
##
time.sleep(0.5)

coordenada1 = 550, 600
coordenada2 = 650, 600
coordenada3 = 760, 600
coordenada4 = 865, 600

count = 0

speed = 1

# coordenadaMouse1 = 550, 650
# coordenadaMouse2 = 650, 650
# coordenadaMouse3 = 760, 650
# coordenadaMouse4 = 865, 650

print('Started...')
while (True):
    monitor = mss().monitors[0]
    sct_img = mss().grab(monitor)
    im = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

    if (im.getpixel(coordenada1) < (54, 100, 255)):
        pyautogui.click(550, 650 * speed)
    elif (im.getpixel(coordenada2) < (54, 100, 255)):
        pyautogui.click(650, 650 * speed)
    elif (im.getpixel(coordenada3) < (54, 100, 255)):
        pyautogui.click(760, 650 * speed)
    elif (im.getpixel(coordenada4) < (54, 100, 255)):
        pyautogui.click(865, 650 * speed)

    count = count + 1
    if(count == 350):
        speed = speed + 0.01
    # print(speed)
