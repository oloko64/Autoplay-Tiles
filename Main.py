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

print('Started...')
while (True):

    monitor = mss().monitors[0]
    sct_img = mss().grab(monitor)
    # Convert to PIL/Pillow Image
    im = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')

    if (im.getpixel(coordenada1) == (0, 0, 0)):
        # print(f'TILE FOUND at {coordenada1} or 1 TILE')
        pyautogui.click(coordenada1)
    elif (im.getpixel(coordenada2) == (0, 0, 0)):
        # print(f'TILE FOUND at {coordenada2} or 2 TILE')
        pyautogui.click(coordenada2)
    elif (im.getpixel(coordenada3) == (0, 0, 0)):
        # print(f'TILE FOUND at {coordenada3} or 3 TILE')
        pyautogui.click(coordenada3)
    elif (im.getpixel(coordenada4) == (0, 0, 0)):
        # print(f'TILE FOUND at {coordenada4} or 4 TILE')
        pyautogui.click(coordenada4)

    elif (im.getpixel(coordenada1) == (16, 20, 19)):
        # print(f'TILE FOUND at {coordenada1} or 1 TILE')
        pyautogui.click(coordenada1)
    elif (im.getpixel(coordenada2) == (16, 20, 19)):
        # print(f'TILE FOUND at {coordenada2} or 2 TILE')
        pyautogui.click(coordenada2)
    elif (im.getpixel(coordenada3) == (16, 20, 19)):
        # print(f'TILE FOUND at {coordenada3} or 3 TILE')
        pyautogui.click(coordenada3)
    elif (im.getpixel(coordenada4) == (16, 20, 19)):
        # print(f'TILE FOUND at {coordenada4} or 4 TILE')
        pyautogui.click(coordenada4)

    # print(color)
    # print(f'LOOP {count}')
    # count = count + 1
    # aux = False

