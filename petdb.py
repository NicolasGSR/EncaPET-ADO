"""Script para criação do banco de dados necessario para testes no localhost
   >>>>>LEMBRAR DE IMPLEMENTAR IMAGENS NO BANCO DE DADOS<<<<<
"""

import mysql.connector
from mysql.connector import errorcode

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='192.168.0.85',
            user='nicolassreis',
            password='senhauser'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `pet_db`;")

cursor.execute("CREATE DATABASE `pet_db`;")

cursor.execute("USE `pet_db`;")

TABLES = {}
TABLES['User'] = ('''
      CREATE TABLE `user` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,      
      `senha` varchar(12) NOT NULL,
      `email` varchar(50) NOT NULL,
      `cep` varchar(8) NOT NULL,
      `telefone` varchar(12) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Pet'] = ('''
      CREATE TABLE `pet` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(20) NOT NULL,
      `idade` varchar(2) NOT NULL,
      `descricao` varchar(200) NOT NULL,
      `especie` varchar(50) NOT NULL,
      `raca` varchar(50) NOT NULL,
      `sexo` varchar(12) NOT NULL,
      `porte` varchar(12) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

conn.commit()

cursor.close()
conn.close()