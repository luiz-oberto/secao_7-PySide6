# QWidegt e QLayout de PySide6.QtWidgets
# QWidget -> genrérico
# QLayout -> um widget de layout que recebe outros widgets
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QVBoxLayout, QHBoxLayout, QGridLayout
'''
QVBoxLayout -> layout na Vertical
QHBoxLayout -> layout na Horizontal
QGridLayout -> 
''' 

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 80px;')

botao2 = QPushButton('Botão 2')
botao2.setStyleSheet('font-size: 40px;')

botao3 = QPushButton('Botão 3')
botao3.setStyleSheet('font-size: 40px;')

central_widget = QWidget() # Serve para exibir várias coisas na tela

layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1, 2)

central_widget.show() # Central Widget entre na hierarquia e mostre sua janela
app.exec() # O loop da aplicação
