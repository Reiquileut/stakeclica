import pyautogui
import time

try:
    while True:
        x, y = pyautogui.position()
        print(f'Posição do mouse - X: {x}, Y: {y}')
        time.sleep(1)  # Espera 1 segundo antes de ler novamente a posição do mouse
except KeyboardInterrupt:
    print('\nPrograma encerrado pelo usuário.')
