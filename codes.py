import cv2
import numpy as np
import keyboard
import mouse
import PIL.ImageGrab
import time


isRun=True
mouse.move(100,100)
mouse.click('right')
time.sleep(5)
while isRun:
    buldumuSol=False
    buldumuSag = False
    mesafeSol=0
    mesafeSag=0
    if keyboard.is_pressed('y'):
        isRun=False
    ss = PIL.ImageGrab.grab(bbox=[300,300,700,650])
    frameGray = cv2.cvtColor(np.array(ss),cv2.COLOR_RGB2GRAY)

    frameGray = cv2.resize(frameGray,(500,500),fx=1,fy=1)
    frameGray[0:100, 0:500] = 0
    median = np.median(frameGray)
    lower1= int(max(0,0.67*median))
    upper1=int(min(255,1.33*median))
    kenarGRay = cv2.Canny(frameGray,lower1,upper1)
    kenarGRay[150:350,270]=255
    kenarGRay[150,220:320]=255
    kenarGRay[350, 220:320] = 255
    kenarGRay[150:350, 220] = 255
    kenarGRay[150:350, 270] = 255
    kenarGRay[150:350, 320] = 255
    for asagı in range(1,200):
        if buldumuSag==False:
            for sag in range(1,50):
                if kenarGRay[150+asagı,270+sag]==255:
                    buldumuSag=True
                    mesafeSag=sag
                    break
        else:
            break
    for asagı in range(1,200):
        if buldumuSol==False:
            for sol in range(1,50):
                if kenarGRay[150+asagı,270-sol]==255:
                    mesafeSol=sol
                    buldumuSol=True
                    break
        else:
            break
    if buldumuSol==True and buldumuSag==True:
        pass
    elif buldumuSol==True and buldumuSag==False:
        keyboard.release('w')
        keyboard.press('s')
        keyboard.press('d')
        print("press D")
        time.sleep(0.18/mesafeSol)
        keyboard.release('d')
        keyboard.release('s')
    elif buldumuSol==False and buldumuSag==True:
        keyboard.release('w')
        keyboard.press('s')
        keyboard.press('a')
        print("press a")
        time.sleep(0.18/mesafeSag)
        keyboard.release('a')
        keyboard.release('s')
    else:
        keyboard.press('w')
        print("press W")
    cv2.imshow('view',kenarGRay)
    cv2.waitKey(30)
