create database if not exists bd_cadastro;

use bd_cadastro;

create table cliente(id_cliente integer primary key auto_increment,
					nome varchar(25),
                    sobrenome varchar(25),
                    idade integer,
                    data_nasc date,
                    email varchar(100),
                    apelido varchar(15),
                    obs varchar(255));
drop table cliente;
show databases;
show tables;
desc cliente;

select * from cliente;








