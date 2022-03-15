import sqlite3
arq = "database.db"
conn = sqlite3.connect(arq)
cursor = conn.cursor()

sql = """CREATE TABLE IF NOT EXISTS professor (
          id integer PRIMARY KEY AUTOINCREMENT,
          nome VARCHAR(30),
          disciplina VARCHAR(20),
          turma VARCHAR(20)
        );"""
cursor.execute(sql)

#### INSERT ####
def inserir():
  t1 = input('Nome:')
  t2 = input('Disciplina:')
  t3 = input('Turma:')
  cursor.execute("INSERT INTO professor (nome, disciplina, turma) VALUES (?,?,?)", (t1, t2, t3))
  conn.commit()

#### UPDATE ####
def atualizar():
  idi = input('Escolha o id:')
  nnome = input('Novo nome:')
  cursor.execute("""UPDATE professor 
  SET nome = ?
  WHERE id = ?""", (nnome, idi))

#### DELETE ####
def deletar():
  var = int(input('Digite id para deletar:'))
  cursor.execute("DELETE FROM professor WHERE id = ?", (var,))

#### SELECT #####
def buscar():
  cursor.execute("SELECT * FROM professor")
  for i in cursor.fetchall():
    print(i)

op = 1
while op != 0:
  print(f"""
  ### CONTROLE DE PROFESSORES ###
  1 - Adicionar Professor
  2 - Mudar Nome de Professor
  3 - Deletar Professor
  4 - Exibir Professores cadastrados
  0 - Sair do Programa
  """)
  op = int(input('Escolha sua opção:'))
  if op == 1:
    print('1')
    inserir()
    op2 = input("Deseja visualizar o cadastro? s/n")
    if op2 == "s":
      buscar()
  elif op == 2:
    print('2')
    atualizar()
  elif op == 3:
    print('3')
    deletar()
  elif op == 4:
    print('4')
    buscar()
  else:
    print('Opção Inválida, tente novamente')

conn.close()
