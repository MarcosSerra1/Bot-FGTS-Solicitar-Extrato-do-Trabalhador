import sys

from PyQt6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
                             QVBoxLayout, QWidget)

from utils.escolha import (abrir_chrome, acessar_site, opcao_extrato,
                           selecionar_certificado)
from utils.extrato_fgts import extratoFGTS


class AutoConnectGUI(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Widgets
        self.label_arquivo = QLabel('Arquivo:')
        self.lineEdit_arquivo = QLineEdit()
        self.button_selecionar_arquivo = QPushButton('Selecionar Arquivo')
        self.label_base_conta = QLabel('Base Conta:')
        self.lineEdit_base_conta = QLineEdit()
        self.label_tipo_extrato = QLabel('Tipo de Extrato:')
        self.lineEdit_tipo_extrato = QLineEdit()
        self.button_extrato_fgts = QPushButton('Extrato FGTS')
        self.button_chave_fgts = QPushButton('Chave FGTS')
        self.button_sair = QPushButton('Sair')

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.label_arquivo)
        layout.addWidget(self.lineEdit_arquivo)
        layout.addWidget(self.button_selecionar_arquivo)
        layout.addWidget(self.label_base_conta)
        layout.addWidget(self.lineEdit_base_conta)
        layout.addWidget(self.label_tipo_extrato)
        layout.addWidget(self.lineEdit_tipo_extrato)
        layout.addWidget(self.button_extrato_fgts)
        layout.addWidget(self.button_chave_fgts)
        layout.addWidget(self.button_sair)

        # Conectar sinais aos slots
        # self.button_selecionar_arquivo.clicked.connect(self.selecionar_arquivo)
        self.button_extrato_fgts.clicked.connect(self.executar_extrato_fgts)
        self.button_chave_fgts.clicked.connect(self.executar_chave_fgts)
        self.button_sair.clicked.connect(self.close)

        # Setar o layout principal
        self.setLayout(layout)

        # Configurações da janela
        self.setWindowTitle('AutoConnect Bot GUI')
        self.setGeometry(100, 100, 400, 300)

    # def selecionar_arquivo(self):
        # options = QFileDialog.Options()
        # options |= QFileDialog.ReadOnly
        # file_name, _ = QFileDialog.getOpenFileName(
        #     self, 'Selecionar Arquivo Excel', '',
        #     'Excel Files (*.xlsx);;All Files (*)', options=options)
        # if file_name:
        #     self.lineEdit_arquivo.setText(file_name)

    def executar_extrato_fgts(self):
        # Adicione a lógica para executar o extrato FGTS
        nome_trabalhador = input("Digite o nome do trabalhador: ")
        base_conta = input("Digite a base da conta: ")
        abrir_chrome()
        acessar_site()
        selecionar_certificado(3)
        opcao_extrato()
        extratoFGTS(nome_trabalhador, base_conta)

    def executar_chave_fgts(self):
        # Adicione a lógica para executar a chave FGTS
        pass


def main():
    app = QApplication(sys.argv)
    gui = AutoConnectGUI()
    gui.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
