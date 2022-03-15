import sqlite3

arquivo_db = "database_db"

conexao = sqlite3.connect(arquivo_db)

criar_tabela = """ CREATE TABLE IF NOT EXISTS alunos (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        nome text NOT NULL,
                        nota integer NOT NULL
                      ); """

cursor = conexao.cursor()
cursor.execute(criar_tabela)

#inserir aluno na tabela
sql_inserir_aluno_felipe = "INSERT INTO alunos (nome, nota) VALUES ('Felipe',10)"
cursor.execute(sql_inserir_aluno_felipe)
conexao.commit() #grava no banco - na tabela

# buscar aluno no banco
sql_buscar_aluno = "SELECT * FROM alunos"
cursor.execute(sql_buscar_aluno)
alunos = cursor.fetchall() #retornar a informação do banco

#encerrar a conexão
conexao.close()

for i in alunos:
    print(f"O aluno {i[1]} tirou a nota {i[2]}")


import mysql.connector

db_connection = mysql.connector.connect(host="localhost", user="root", passwd="", database="bd")
cursor = db_connection.cursor()