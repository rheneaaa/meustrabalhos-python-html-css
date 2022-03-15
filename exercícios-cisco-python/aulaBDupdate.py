import sqlite3

arq = "database.db"
conn = sqlite3.connect(arq)
cursor = conn.cursor()

# Exemplo 1
sql = """CREATE TABLE IF NOT EXISTS professor (
    id integer PRIMARY KEY AUTOINCREMENT,
    nome text,
    disciplina test,
    turma text
    );"""

cursor.execute(sql)

#### INSERT ####
cod = "INSERT INTO professor (nome, disciplina, turma) VALUES ('Daniel', 'Programação', 'Técnico')"
cursor.execute(cod)

# Exemplo 2
v1 = "Diego"
v2 = "Banco de Dados"
v3 = "Análise de Siatemas"
cursor.execute("INSERT INTO professor (nome, disciplina, turma) VALUES (?,?,?)", (v1, v2, v3))

# Exemplo 3
t1 = input("Nome")
t2 = input("Disciplina")
t3 = input("Turma")
cursor.execute("INSERT INTO professor (nome, disciplina, turma) VALUES (?, ?, ?)", (t1, t2, t3))

conn.commit()

### UPDATE ###
nnome = input("Nome")
sql = ("""UPDATE professor SET nome = ? WHERE id = 2""",(nnome));

# Delete #
codigo = "DELETE FROM professor WHERE id = 3"
cursor.execute(codigo)

# select #
cursor.execute("SELECT * FROM professor")
for i in cursor.fetchall():
    print(i)

conn.close()
