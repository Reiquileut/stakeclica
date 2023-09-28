import time

import pyautogui
import os


def buscaOperacao():
    #imgCheck = 'LINUX DIRECTORY/src/test/imgBtnEnable.png'
    imgCheck = 'src/tests/imgBtnEnable.png'
    sizeScreen = (pyautogui.size().width / 2)
    valueLeft = '50'
    valueRight = '200'

    try:
        location = list(pyautogui.locateAllOnScreen(imgCheck, confidence=0.8))
        if location:
            for i in location:
                btnPos = float(i.left)
                if btnPos > sizeScreen:
                    alteraValor(i, valueRight)
                    print("Vai Ajustar o lado Direito")
                if btnPos < sizeScreen:
                    alteraValor(i, valueLeft)
                    print("Vai Ajustar o lado Esquerdo")
        else:
            print("Não Encontrou")
    except:
        print("Fodeu")


def alteraValor(item, side):
    pyautogui.click(float(item.left) - 50, float(item.top))
    time.sleep(1)
    pyautogui.typewrite(side, interval=0.5)
    time.sleep(1)
    pyautogui.press('Enter')
    time.sleep(1)
    pyautogui.press('Delete')
