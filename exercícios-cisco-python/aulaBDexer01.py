import sqlite3

arq = "database.db"
conn = sqlite3.connect(arq)
cursor = conn.cursor()


sql = """CREATE TABLE IF NOT EXISTS professor (
    id integer PRIMARY KEY AUTOINCREMENT,
    nome text,
    disciplina test,
    turma text
    );"""

cursor.execute(sql)

class Insert():
    def __init__(self, nome, disciplina, turma):
        self.nome = nome
        self.disciplina = disciplina
        self.turma = turma

    def getNome(self):
        return self.nome
    def getDisciplina(self):
        return self.disciplina
    def getTurma(self):
        return self.turma

    def altNome(self, nvnome):
        self.nome = nvnome
    def altDisciplina(self, nvdisciplina):
        self.disciplina = nvdisciplina
    def altTurma(self, nvturma):
        self.turma = nvturma

novo = Insert("Novo nome", "Nova disciplina", "Nova turma")

nvnome = input("Nome ")
novo.altNome(nvnome)
print("Novo nome: {}".format(nvnome))
nvdisciplina = input("Disciplina ")
novo.altDisciplina(nvdisciplina)
nvturma = input("Turma ")
novo.altTurma(nvturma)
cursor.execute("INSERT INTO professor (nome, disciplina, turma) VALUES (?, ?, ?)", (nvnome, nvdisciplina, nvturma))

conn.commit()

### UPDATE ###
nvnome = input("Nome ")
novo.altNome(nvnome)
sql = ("""UPDATE professor SET nome = ? WHERE id = 2""",(nvnome));

# Delete #
delete = input("Delete ")
codigo = ("DELETE FROM professor WHERE id = ?", delete);
cursor.execute(codigo)

# select #
cursor.execute("SELECT * FROM professor")
for i in cursor.fetchall():
    print(i)

conn.close()
