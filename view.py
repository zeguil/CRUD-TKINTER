import mysql.connector

conexao = mysql.connector.connect(
    host='localhost:3306',
    user='root',
    password='199909',
    database='faculdade',
)

cursor = conexao.cursor()

lista = []

query = "INSERT INTO alunos(nome, email, telefone, nascimento, ativo, UF, cidade) VALUES (?, ?, ?, ?, ?, ?, ?,)"
cursor.execute(query, lista)

#CRUD

# CREATE
# comando = f'INSERT INTO alunos (nome, idade, nascimento) VALUES ("{nome}", "{idade}", "{nascimento}")'
# cursor.execute(comando)

# #READ
# comando = "SELECT * FROM alunos"
# resultado = cursor.fetchall() # ler o banco 
# print(resultado)

# #UPDATE
# comando = f'UPDATE alunos SET valor = {6} WHERE nome = "{lucas}"'
# cursor.execute(comando)
# conexao.commit()

# #DELETE
# comando = f'DELETE FROM alunos WHERE nome = "{}"'
# cursor.execute(comando)
# conexao.commit()

# cursor.close()
# conexao.close()