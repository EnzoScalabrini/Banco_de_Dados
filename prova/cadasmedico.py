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

def insert_BD():
    connection = conectarBD("localhost","root","admin","Hospital") 
    cursor = connection.cursor() 
    nome = tela.txtnome.text()
    email = tela.txtemail.text()
    cpf = tela.txtcpf.text()
    telefone = tela.txttelefone.text() 
    crm = tela.txtcrm.text() 
    rg = tela.txtrg.text()
    sexo = tela.txtsexo.text()
    nascimento = tela.txtdata.text()
    complemento = tela.txtcomplemento.text()
    numerocs = tela.txtnumerocasa.text()
    cep = tela.txtcep.text()
    

    sql = "INSERT INTO Medico (nome, email, telefone, crm, cpf, rg, cep, numerocs, complemento) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (
    nome,
    email,
    telefone,
    crm,
    cpf,
    rg,
    sexo,
    nascimento,
    cep,
    numerocs,
    complemento,
    )

    cursor.execute(sql, data) 
    connection.commit() 

    userid = cursor.lastrowid 

    cursor.close() 
    connection.close() 

    QtWidgets.QMessageBox.about(tela, 'SUCESSO!', "Foi cadastrado o novo medico de ID: " + str(userid))

def read_BD():
    connection = conectarBD("localhost","root","admin","Hospital")
    cursor = connection.cursor() 

    sql = "SELECT nome, endereco FROM medico where CPF="

    cursor.execute(sql) 
    results = cursor.fetchall() 
    for row in results:
        tela.txtnome.settxt(row[1])
        tela.txtEndereco.settxt(row[0])

    cursor.close()
    connection.close() 

def limparr(): 
    tela.txtnome.setText("")
    tela.txtcpf.setText("")
    tela.txtcrm.setText("")
    tela.txtrg.setText("")
    tela.txtcomplemento.setText("")
    tela.txtnumerocasa.setText("")
    tela.txtcep.setText("")
    tela.txtemail.setText("")
    tela.txttelefone.setText("")


def AbrirHospital():
    tela.show()
    #telaMenu.close()


app = QtWidgets.QApplication(sys.argv)
tela = uic.loadUi('Hospital.ui')
#telaConsulta = uic.loadUi('cadastromedic.ui')
#telaMenu = uic.loadUi('cadastromedic.ui')
tela.show()
tela.btncadastrar.clicked.connect(insert_BD)
tela.btnlimparr.clicked.connect(limparr) 
#tela.btncadastrar.clicked.connect(insert_BD)

app.exec() 