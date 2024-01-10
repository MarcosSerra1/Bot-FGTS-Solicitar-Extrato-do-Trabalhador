from time import sleep

import pyautogui as bot

nome_trabalhador = input(' ').upper()
base_conta = 'b'

sleep(5)
bot.click(739, 604, duration=2)  # 739,604 Base da conta
bot.write(base_conta)
bot.press('enter')

sleep(5)
bot.click(732, 633, duration=2)  # 732,633 Nome do Trabalhador
bot.write(nome_trabalhador)

# sleep(5)
bot.click(241, 777, duration=2)  # 241,777 Botão Cotinuar
