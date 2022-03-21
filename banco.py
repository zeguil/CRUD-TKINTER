# criando conexão

import mysql.connector

conexao = mysql.connector.connect(
    host='localhost:3306',
    user='root',
    password='199909',
    database='faculdade',
)

cursor = conexao.cursor()
