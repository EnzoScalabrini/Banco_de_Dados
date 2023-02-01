create database hospital;
use hospital;

create table paciente(
nome VARCHAR(60),
cpf INT(11),
telefone INT(11),
endereco VARCHAR(60),
plano_saude VARCHAR(60),
email varchar (60),
numero int (5),
numero_carteirinha int (20),
cidade varchar(60)
);
select*from paciente 