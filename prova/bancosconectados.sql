create database Hospital;
use Hospital;

create table Medico(
nome varchar (160),
email VARCHAR(240),
telefone int(120),
crm int (250),
cpf int (200),
rg int (60),
cep int (60),
numerocs int (60),
complemento varchar (150));

select * from Medico

create table paciente(
nome varchar(250),
cpf int (100),
telefone int (150),
endereco varchar (450),
plano_saude int (250),
email varchar (250),
numero int (250),
numero_carteirinha int (250),
cidade varchar (250));
select * from paciente

