import time
from threading import Thread
import pyautogui
from PIL import Image
from mss import mss

time.sleep(0.5)
# part of the screen
# aux = True
# count = 1


coordenada1 = 550, 600
coordenada2 = 650, 600
coordenada3 = 760, 600
coordenada4 = 865, 600

imgGlobal = 0

print('started...')

def task():
    global imgGlobal
    
    while(True):
        with mss() as sct:
            monitor = sct.monitors[0]
            sct_img = sct.grab(monitor)
            # Convert to PIL/Pillow Image
            imgGlobal = Image.frombytes('RGB', sct_img.size, sct_img.bgra, 'raw', 'BGRX')


def calc():
    while(True):
        im = imgGlobal
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

# create two new threads
t1 = Thread(target=task)
t2 = Thread(target=calc)
# t3 = Thread(target=task)

# start the threads
t1.start()
t2.start()
# t3.start()
# wait for the threads to complete
t1.join()
t2.join()
# t3.join()

# im.save("box.png")
