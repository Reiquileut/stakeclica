import pyautogui
import time

time.sleep(1)

while True:
    try:
        if   pyautogui.locateOnScreen('stake.png', confidence=0.8):
            qdd = pyautogui.locateCenterOnScreen( 'stake.png', confidence=0.8)

            pyautogui.click(qdd.x,qdd.y)

    except:
        pass