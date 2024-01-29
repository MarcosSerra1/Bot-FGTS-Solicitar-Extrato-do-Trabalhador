'''
Este script extrai dados do conectividade social, incluindo:
    1. Extrato FGTS
    2. Chave FGTS
'''
from utils.escolha import (abrir_chrome, acessar_site, opcao_chave,
                           opcao_extrato, selecionar_certificado)
from utils.extrato_fgts import extratoFGTS


def exibir_menu():
    print("===== MENU =====")
    print("1. Extrato FGTS")
    print("2. Chave FGTS")
    print("0. Sair")


def main():
    while True:
        exibir_menu()

        opcao = input("Escolha uma opção (0-2): ")

        if opcao == '1':
            # Extrato FGTS
            nome_trabalhador = input("Digite o nome do trabalhador: ")
            base_conta = input("Digite a base da conta: ")
            posicao_certificado = input("Digite a posição do certificado: ")
            abrir_chrome()
            acessar_site()
            selecionar_certificado(posicao_certificado)
            opcao_extrato()
            extratoFGTS(nome_trabalhador, base_conta)

        elif opcao == '2':
            # Chave FGTS
            nome_trabalhador = input("Digite o nome do trabalhador: ")
            base_conta = input("Digite a base da conta: ")
            posicao_certificado = input("Digite a posição do certificado: ")
            abrir_chrome()
            acessar_site()
            selecionar_certificado(posicao_certificado)
            opcao_chave()

        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
