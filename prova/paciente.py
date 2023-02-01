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
    connection = conectarBD("localhost","root","admin","hospital")
    cursor = connection.cursor() 
    nome = tela.txtnomep.text()
    cpf = tela.txtcpfp.text()
    telefone = tela.txttelefonep.text()
    endereco = tela.txtenderecop.text()
    plano_saude = tela.txtplanop.text()
    email = tela.txtemail.text()
    numero = tela.txtnumero.text()
    numero_carteirinha = tela.txtnumeroc.text()
    cidade = tela.txtcidade.text()

    sql = "INSERT INTO paciente (nome, cpf, telefone, endereco, plano_saude, email, numero, numero_carteirinha, cidade) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    data = (
    nome,
    cpf,
    telefone,
    endereco,
    plano_saude,
    email,
    numero,
    numero_carteirinha,
    cidade,
    )
    cursor.execute(sql, data) 
    connection.commit() 

    userid = cursor.lastrowid 

    cursor.close() 
    connection.close() 

    QtWidgets.QMessageBox.about(tela, 'SUCESSO!', "Foi cadastrado o novo Paciente de ID: " + str(userid))

def read_BD():
    connection = conectarBD("localhost","root","aulasDB_2022","projeto")
    cursor = connection.cursor() 

    sql = "SELECT nome, endereco FROM Paciente where CPF=" 

    cursor.execute(sql) 
    results = cursor.fetchall() 
    for row in results:
        tela.txtNome.setText(row[1])
        tela.txtEndereco.setText(row[1])

    cursor.close()
    connection.close() 

def Limpar():
    tela.txtnomep.setText("")
    tela.txtcpfp.setText("")
    tela.txttelefonep.setText("")
    tela.txtenderecop.setText("")
    tela.txtplanop.setText("")
    tela.txtemail.setText("")
    tela.txtnumero.setText("")
    tela.txtnumeroc.setText("")
    tela.txtcidade.setText("")

def AbrirTelaPaciente():
    tela.show()
 

app = QtWidgets.QApplication(sys.argv)
tela = uic.loadUi('TelaPaciente.ui')
tela.btncadastrar.clicked.connect(AbrirTelaPaciente)
tela.show()
tela.btnlimpar.clicked.connect(Limpar)
tela.btncadastrar.clicked.connect(insert_BD)
app.exec()
