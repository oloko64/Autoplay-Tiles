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
# part of the screen
# aux = True
# count = 1

coordenada1 = 550, 600
coordenada2 = 650, 600
coordenada3 = 760, 600
coordenada4 = 865, 600

coordenadaMouse1 = 550, 650
coordenadaMouse2 = 650, 650
coordenadaMouse3 = 760, 650
coordenadaMouse4 = 865, 650

print('Started...')
while (True):
    monitor = mss().monitors[0]
    sct_img = mss().grab(monitor)
    # Convert to PIL/Pillow Image
    im = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

    if (im.getpixel(coordenada1) < (54, 100, 255)):
        # print(f'TILE FOUND at {coordenada1} or 1 TILE')
        pyautogui.click(coordenadaMouse1)
    elif (im.getpixel(coordenada2) < (54, 100, 255)):
        # print(f'TILE FOUND at {coordenada2} or 2 TILE')
        pyautogui.click(coordenadaMouse2)
    elif (im.getpixel(coordenada3) < (54, 100, 255)):
        # print(f'TILE FOUND at {coordenada3} or 3 TILE')
        pyautogui.click(coordenadaMouse3)
    elif (im.getpixel(coordenada4) < (54, 100, 255)):
        # print(f'TILE FOUND at {coordenada4} or 4 TILE')
        pyautogui.click(coordenadaMouse4)

    # print(color)
    # print(f'LOOP {count}')
    # count = count + 1
    # aux = False

