# criando conexão

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='',
    password='',
    database='faculdade',
)

cursor = conexao.cursor()
