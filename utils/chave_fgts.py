# extrato_fgts.py
import os
from time import sleep

import pyautogui as bot

from utils.pasta_util import criar_pasta


def chaveFGTS(nome_trabalhador, base_conta):
    '''
    Função para imprimir a chave do FGTS, interagindo
    com o conectividade social.

    Args:
        nome_trabalhador (str): Nome do trabalhador.
        base_conta (str): Informações relacionadas à conta.

    Returns:
        bool:
        True se a operação foi concluída com sucesso,
        False se ocorreu um erro.
    '''

    try:
        # Converter o nome do trabalhador para letras maiúsculas
        nome_trabalhador = nome_trabalhador.upper()

        # Iniciar a interação com o conectividade social
        sleep(10)
        bot.click(1494, 901, duration=1)
        tab(12)
        sleep(7)
        bot.write(base_conta)  # base da conta

        tab(1)
        bot.write(nome_trabalhador)  # nome do trabalhador

        sleep(5)
        tab(6)  # botão continuar
        bot.press('enter')

        sleep(5)
        # logica para colocar data de movimentação

        # Criar a pasta para armazenar os documentos
        diretorio_downloads = os.path.expanduser('~') + '/Downloads'
        caminho_pasta_fgts = os.path.join(diretorio_downloads, 'FGTS')
        sleep(10)
        if criar_pasta(caminho_pasta_fgts):
            # Configurar o caminho completo para o documento
            caminho_documento = os.path.join(
                caminho_pasta_fgts, f'EXTRATO FGTS {nome_trabalhador}.pdf')

            # Configurar o caminho completo para o documento
            bot.click(1300, 69, duration=1)  # Caminho da pasta FGTS
            bot.press('delete')
            bot.write(caminho_pasta_fgts)
            bot.press('enter')

            # Configurar o nome do documento
            sleep(5)
            # Cordenada para colocar o Nome do Documento
            bot.click(788, 886, duration=1)
            bot.write(f'EXTRATO FGTS {nome_trabalhador}')  # nome do documento
            bot.press('enter')

            print(f"Extrato do FGTS salvo em: {caminho_documento}")
            return True
        else:
            return False

    except Exception as e:
        print(f"Erro ao extrair o extrato do FGTS: {e}")
        return False


def tab(cliques):
    bot.press('tab', cliques)
