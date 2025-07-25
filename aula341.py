# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O widget principal da aplicação
# QpushButton -> um botão
# PySide6.QtWidgets -> kOnde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')
botao.show() # Adiciona o widget na hieraquia e exibe a janela

botao2 = QPushButton('Botão 2')
botao2.show()

app.exec() # O loop da aplicação
