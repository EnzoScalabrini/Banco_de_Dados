from PyQt5 import uic, QtWidgets
import sys
import os
os.system("pip install mysql-connector-python")
import mysql.connector

def conectarBD(host, usuario, senha, DB):
    connection = mysql.connector.connect( 
        host = host, 
        user= usuario, 
        password=senha, 
        database=DB  
    ) 
    return connection

def Hospital.ui 
btnMedico.connect(Hospital.ui)

def AbrirHospital():
    tela.show()
    #telaMenu.close()

def TelaMenu():
    btnMedico.clicked.connect(Hospital)
    tela.show()



app = QtWidgets.QApplication(sys.argv)
tela = uic.loadUi('TelaMenu.ui')
telaPaciente = uic.loadUi('Telapaciente.ui')
Hospital = uic.loadUi('Hospital.ui')
tela.show()

app.exec() 