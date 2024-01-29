import os
from time import sleep

import pyautogui as bot
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from utils.pasta_util import criar_pasta
from utils.selecionar_certificado import selecionarCertificado, tab


def extratoFGTS(base_conta, nome_trabalhador):
    '''
    Função para imprimir o extrato do FGTS, interagindo com o Conectividade Social.

    Args:
        nome_trabalhador (str): Nome do trabalhador.
        base_conta (str): Informações relacionadas à conta.

    Returns:
        bool: True se a operação foi concluída com sucesso, False se ocorreu um erro.
    '''
    try:
        # Inicia o serviço do Chrome WebDriver
        service = Service()

        # Configurações do Chrome WebDriver
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
        driver.maximize_window()

        # URL do Conectividade Social ICP V2
        url = 'https://conectividadesocialv2.caixa.gov.br/sicns/'

        # Abre a URL no navegador controlado pelo Selenium
        driver.get(url)

        # Aguarda 20 segundos antes de clicar no botão "Empregador"
        sleep(20)
        BTN_EMPREGADOR = 'btnEmpregador'
        CLIQUE_BTN_EMPREGADOR = driver.find_element(By.ID, BTN_EMPREGADOR).click()

        # Seleciona o certificado usando a função externa
        selecionarCertificado(3)

        # Aguarda 30 segundos após a seleção do certificado
        sleep(30)

        # Barra de seleção para escolher o serviço desejado
        INPUT_BARRA_SELECAO = "/html/body/form/table[2]/tbody/tr[1]/td[3]/table/tbody/tr/td[1]/select"
        CLIQUE_INPUT_BARRA_SELECAO = driver.find_element(
            By.XPATH, INPUT_BARRA_SELECAO)
        if CLIQUE_INPUT_BARRA_SELECAO.is_displayed():
            CLIQUE_INPUT_BARRA_SELECAO.click()
        else:
            print("O campo para selecionar o serviço desejado não está visível!")

        driver.find_element(By.XPATH, INPUT_BARRA_SELECAO).send_keys(
            Keys.ARROW_DOWN * 11)
        sleep(1)
        driver.find_element(
            By.XPATH, INPUT_BARRA_SELECAO).send_keys(Keys.ENTER)

        # Aguarda 40 segundos após a seleção do serviço
        sleep(40)

        # Barra de seleção para escolher a base da conta
        INPUT_BASE_CONTA = "/html/body/form/table[2]/tbody/tr[3]/td[3]/p/table/tbody/tr[3]/td[2]/select"
        CLIQUE_INPUT_BASE_CONTA = driver.find_element(
            By.XPATH, INPUT_BASE_CONTA)
        if CLIQUE_INPUT_BASE_CONTA.is_displayed():
            CLIQUE_INPUT_BASE_CONTA.click()
        else:
            print("O campo para selecionar a base da conta não está visível!")

        # Insere as informações da base da conta
        driver.find_element(By.XPATH, INPUT_BASE_CONTA).send_keys(base_conta)
        driver.find_element(By.XPATH, INPUT_BASE_CONTA).send_keys(Keys.ENTER)

        sleep(5)

        # Barra de entrada para o nome do trabalhador
        INPUT_NOME_TRABALHADOR = "/html/body/form/table[2]/tbody/tr[3]/td[3]/p/table/tbody/tr[7]/td[2]/input"
        CLIQUE_INPUT_NOME_TRABALHADOR = driver.find_element(
            By.XPATH, INPUT_NOME_TRABALHADOR)
        if CLIQUE_INPUT_NOME_TRABALHADOR.is_displayed():
            CLIQUE_INPUT_NOME_TRABALHADOR.click()
        else:
            print("O campo para selecionar o nome do trabalhador não está visível!")

        # Insere o nome do trabalhador
        sleep(2)
        driver.find_element(By.XPATH, INPUT_NOME_TRABALHADOR).send_keys(nome_trabalhador)
        driver.find_element(By.XPATH, INPUT_NOME_TRABALHADOR).send_keys(Keys.ENTER)

        sleep(10)
        bot.click(1807, 315, duration=0.1)

        # Seleciona o botão de visualizar impressão
        tab(13)
        bot.press('enter')

        # Clica no botão de imprimir
        sleep(10)
        tab(1)
        bot.press('enter')

        # Clica no botão de imprimir na janela pop-up
        sleep(6)
        bot.press('enter')

        # Aguarda 10 segundos antes de continuar
        sleep(10)

        try:
            # Cria a pasta para armazenar os documentos
            diretorio_downloads = os.path.expanduser('~') + '/Downloads'
            caminho_pasta_fgts = os.path.join(diretorio_downloads, 'FGTS')

            # Aguarda 20 segundos antes de criar a pasta
            sleep(20)

            # Se a pasta for criada com sucesso
            if criar_pasta(caminho_pasta_fgts):
                # Configura o caminho completo para o documento
                caminho_documento = os.path.join(
                    caminho_pasta_fgts, f'EXTRATO FGTS {nome_trabalhador}.pdf')

                # Aguarda 5 segundos antes de continuar
                sleep(5)

                # Clica no ícone da pasta FGTS
                bot.click(1300, 69, duration=1)
                bot.press('delete')
                bot.write(caminho_pasta_fgts)
                bot.press('enter')

                # Aguarda 5 segundos antes de continuar
                sleep(5)

                # Clica no campo para inserir o nome do documento
                bot.click(788, 886, duration=1)
                bot.write(f'EXTRATO FGTS {nome_trabalhador}')
                bot.press('enter')

                print(f"Extrato do FGTS salvo em: {caminho_documento}")
                return True
            else:
                return False

        except Exception as e:
            print(f"Erro ao extrair o extrato do FGTS: {e}")
            return False

    except Exception as e:
        print(f"Erro ao extrair o extrato do FGTS: {e}")
        return False

    finally:
        driver.quit()

extratoFGTS('b','RAELY KATTARINE FREITAS MOTA COSTA')
