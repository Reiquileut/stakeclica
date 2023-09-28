import pyautogui
import time

from utils import buscaOperacao

# Define o horário de início e término e constantes
img = '/home/ubuntu/PycharmProjects/stakeclica/src/stake.png'
#img = 'src/tests/imgBtnEnable.png'
hora_inicio = 7  # 4 da manhã
hora_termino = 23  # termina as 20 da noite

while True:
    time.sleep(2)  # Verifica a cada 2 segundos
    # Obtém a hora atual
    hora_atual = time.localtime().tm_hour

    # Verifica se está dentro do intervalo de tempo desejado
    if hora_inicio <= hora_atual < hora_termino:
        try:
            print("VAI BUSCAR:" + str(time.time()))
            if pyautogui.locateOnScreen(img, confidence=0.8):
                buscaOperacao()
                qdd = pyautogui.locateCenterOnScreen(img, confidence=0.8)
                pyautogui.click(qdd.x, qdd.y)

        except Exception as e:
            print(f"Erro: {e}")

    # Aguarda um período de tempo antes de verificar novamente (ajuste conforme necessário)



