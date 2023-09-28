import time

import pyautogui
import os


def buscaOperacao():
    imgCheck = '/home/ubuntu/PycharmProjects/stakeclica/src/botao2.png'
    # imgCheck = 'src/tests/imgBtnEnable.png'
    sizeScreen = (pyautogui.size().width / 2)
    valueLeft = '0.01'
    valueRight = '0.03'

    # while True:
    # time.sleep(5)
    try:
        location = list(pyautogui.locateAllOnScreen(imgCheck, confidence=0.99))
        if location:
            for i in location:
                btnPos = float(i.left)
                if btnPos > sizeScreen:
                    alteraValor(i, valueRight)
                    print("Vai Ajustar o lado Direito")
                if btnPos < sizeScreen:
                    alteraValor(i, valueLeft)
                    print("Vai Ajustar o lado Esquerdo")
            return
        else:
            print("Não Encontrou")
            return
    except:
        print("Fodeu")
        return


def alteraValor(item, side):
    pyautogui.click(float(item.left), float(item.top))
    time.sleep(2)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('delete')
    pyautogui.typewrite(side, interval=1)
    pyautogui.click(float(item.left), float(item.top) -30)
    return
# time.sleep(1)
# pyautogui.press('Enter')
# return
# time.sleep(1)
# pyautogui.press('Delete')

#buscaOperacao()
