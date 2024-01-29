from time import sleep

import pyautogui as bot


def tab(cliques):
    '''
    Simula pressionar a tecla 'Tab' várias vezes usando a biblioteca PyAutoGUI.

    Args:
        cliques (int): O número de cliques na tecla 'Tab'.

    Returns:
        None
    '''

    bot.press('tab', cliques)


def selecionarCertificado(certificado_index):
    '''
    Seleciona um certificado em uma lista por índice.

    Args:
        certificado_index (int): O índice do certificado a ser selecionado.

    Returns:
        None
    '''

    # Converte o índice do certificado para inteiro
    certificado_index = int(certificado_index)

    # Navega até o certificado desejado na lista e pressiona
    # Enter para selecioná-lo
    sleep(5)
    bot.press('down', certificado_index)
    bot.press('enter')

    # Aguarda mais 10 segundos antes de confirmar a seleção
    sleep(10)
    bot.press('down', certificado_index)
    bot.press('enter')
