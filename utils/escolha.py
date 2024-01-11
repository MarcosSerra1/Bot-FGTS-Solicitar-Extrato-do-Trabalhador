# Importa o módulo sleep da biblioteca time para adicionar pausas no código
from time import sleep

# Importa a biblioteca pyautogui para interagir com a
# interface gráfica do usuário
import pyautogui as bot


# Função para navegar entre os campos usando a tecla Tab
def tab(cliques):
    bot.press('tab', cliques)


# Função para abrir o navegador Chrome
def abrir_chrome():
    # Aguarda 5 segundos antes de abrir o Chrome
    sleep(5)

    # Simula o pressionamento de teclas para abrir o executador
    # de comandos no Windows
    bot.keyDown('win')
    bot.keyDown('r')
    bot.keyUp('win')
    bot.keyUp('r')

    # Apaga o conteúdo da caixa de diálogo e digita 'chrome'
    bot.press('delete')
    bot.write('chrome')

    # Pressiona Enter para abrir o navegador Chrome
    bot.press('enter')


# Função para acessar um site específico
def acessar_site():
    # Aguarda 2 segundos antes de executar a próxima ação
    sleep(2)

    # Navega até a caixa de diálogo de execução de comandos
    tab(1)

    # Pressiona Enter para abrir o navegador com o site fornecido
    bot.press('enter')

    # Aguarda 2 segundos antes de executar a próxima ação
    sleep(2)

    # Digita o URL do site e pressiona Enter para acessá-lo
    bot.write('https://conectividadesocialv2.caixa.gov.br/sicns/')
    bot.press('enter')


# Função para selecionar um certificado específico
def selecionar_certificado(certificado_index):
    # Converte o índice do certificado para inteiro
    certificado_index = int(certificado_index)

    # Aguarda 5 segundos antes de executar a próxima ação
    sleep(5)

    # Navega até a opção do certificado no menu
    tab(8)

    # Pressiona Enter para abrir a lista de certificados
    bot.press('enter')

    # Aguarda 10 segundos antes de selecionar o certificado desejado
    sleep(10)

    # Navega até o certificado desejado na lista e pressiona
    # Enter para selecioná-lo
    bot.press('down', certificado_index)
    bot.press('enter')

    # Aguarda mais 10 segundos antes de confirmar a seleção
    sleep(10)
    bot.press('down', certificado_index)
    bot.press('enter')


# Função para escolher a opção de extrato no Conectividade Social
def opcao_extrato():
    # Aguarda 20 segundos antes de executar a próxima ação
    sleep(20)

    # Navega até a opção de extrato no menu
    tab(9)

    # Pressiona Enter para escolher a opção de extrato do trabalhador
    bot.press('enter')

    # Aguarda 2 segundos antes de selecionar o tipo de extrato desejado
    sleep(2)
    bot.press('down', 11)

    # Pressiona Enter para confirmar a seleção
    bot.press('enter')


# Função para escolher a opção de chave no Conectividade Social
def opcao_chave():
    # Aguarda 5 segundos antes de executar a próxima ação
    sleep(5)

    # Navega até a opção de chave no menu
    tab(9)

    # Pressiona Enter para escolher a opção de chave do trabalhador
    bot.press('enter')

    # Aguarda 2 segundos antes de selecionar o tipo de chave desejado
    sleep(2)
    bot.press('down', 3)

    # Pressiona Enter para confirmar a seleção
    bot.press('enter')


# # Código comentado abaixo é um exemplo de como usar as funções acima

# # # Abrir o navegador Chrome
# abrir_chrome()

# # # Acessar o site do Conectividade Social
# acessar_site()

# # # Selecionar o certificado desejado (índice 3 no exemplo)
# selecionar_certificado(3)

# # # Escolher opção de extrato
# opcao_extrato()
