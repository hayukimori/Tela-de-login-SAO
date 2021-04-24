# coding: utf-8

#Bibliotecas: PyQt5, os (UNIX), PyGame
import os
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import *

#PyGame também é importado apenas para carregar os audios
from pygame import mixer as mx


# Iniciando módulo de áudio para ser usado mais tarde
mx.init()


def start_login():
	# Transformar todos os caracteres de LineEdit em Asteríscos

	login.account_line.setEchoMode(QLineEdit.Password)
	login.password_line.setEchoMode(QLineEdit.Password)



	# deixando no centro
	rectangle_frame = login.frame.frameGeometry()
	rectangle_frame.moveCenter(centerPoint)
	login.frame.move(rectangle_frame.topLeft())




	# Mostrar tela
	login.showFullScreen()



def loadedcharacter():

	# carregando e tocando efeito
	mx.music.load('select.ogg')
	mx.music.play()

	# Fechar janela de login
	login.close()



	# Pegar username direto do terminal
	username = os.getenv("USER")


	# Colocar espaço entre as letras do nome do usuário
	result = ''
	for ch in username:
		result = result + ch + ' '


	# Inserir o nome do usuário + a edição
	loaded_character.charactername.setText(f"{result} (A)")



	#deixar no centro
	rectangle_frame = loaded_character.frame.frameGeometry()

	rectangle_frame.moveCenter(centerPoint)
	loaded_character.frame.move(rectangle_frame.topLeft())



	# Mostrar a janela de personagem beta carregado
	loaded_character.showFullScreen()




def welcome():

	# tocando efeitos
	mx.music.load('select.ogg')
	mx.music.play()

	# Fechar janela de beta carregado
	loaded_character.close()



	# Mostrar a janela de welcome em fullscreen
	mx.music.load('welcome.ogg')
	mx.music.play()

	welcome_window.showFullScreen()





app = QtWidgets.QApplication([])




# Carregando janelas
login				= uic.loadUi("login_window.ui")
loaded_character	= uic.loadUi("loaded_character.ui")
welcome_window		= uic.loadUi("welcome_window.ui")








# Sem bordas
login.setWindowFlags(Qt.FramelessWindowHint)
loaded_character.setWindowFlags(Qt.FramelessWindowHint)


# Sem Background
login.setAttribute(Qt.WA_TranslucentBackground);
loaded_character.setAttribute(Qt.WA_TranslucentBackground)
welcome_window.setAttribute(Qt.WA_TranslucentBackground)





# Colocando sombra
shadow = QGraphicsDropShadowEffect()
shadow.setBlurRadius(20)
shadow.setXOffset(0)
shadow.setYOffset(0)
shadow.setColor(QColor(0,0,0,90))
login.frame.setGraphicsEffect(shadow)
loaded_character.frame_cima.setGraphicsEffect(shadow)
loaded_character.frame_central.setGraphicsEffect(shadow)




#Deixando no centro
qtRectangle			= login.frameGeometry()
qtRectangle_ldc		= loaded_character.frameGeometry()
qtRectangle_wlc		= welcome_window.frameGeometry()
centerPoint			= QDesktopWidget().availableGeometry().center()

qtRectangle.moveCenter(centerPoint)
qtRectangle_ldc.moveCenter(centerPoint)
qtRectangle_wlc.moveCenter(centerPoint)

login.move(qtRectangle.topLeft())
loaded_character.move(qtRectangle_ldc.topLeft())
welcome_window.move(qtRectangle_wlc.topLeft())






# Mostrando para o usuário
start_login()




# Se os botões forem pressionados
login.loginbutton.clicked.connect(loadedcharacter)
loaded_character.OK.clicked.connect(welcome)
loaded_character.NO.clicked.connect(welcome)


app.exec()
