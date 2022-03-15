import sqlite3
arq = "tabelamusicas.db"
conn = sqlite3.connect(arq)
cursor = conn.cursor()

sql = """CREATE TABLE IF NOT EXISTS musicas (
          id integer PRIMARY KEY AUTOINCREMENT,
          nome VARCHAR(30),
          artista VARCHAR(20),
          genero VARCHAR(20),
          duracao float
        );"""
cursor.execute(sql)

#### INSERT ####
def inserir():
  t1 = input('Insira uma música: ')
  t2 = input('Nome do artista: ')
  t3 = input('Gênero: ')
  t4 = float(input("Duração: "))
  cursor.execute("INSERT INTO musicas (nome, artista, genero, duracao) VALUES (?,?,?,?)", (t1, t2, t3, t4))
  conn.commit()

#### UPDATE ####
def atualizar():
  idi = input('Escolha o id:')
  nnome = input('Nova música:')
  cursor.execute("""UPDATE musicas 
    SET nome = ?
    WHERE id = ?""", (nnome, idi))
  art = input('Novo artista: ')
  cursor.execute("""UPDATE musicas 
    SET artista = ?
    WHERE id = ?""", (art, idi))
  gen = input('Novo gênero: ')
  cursor.execute("""UPDATE musicas 
    SET genero = ?
    WHERE id = ?""", (gen, idi))
  dur = float(input('Nova duração: '))
  cursor.execute("""UPDATE musicas 
    SET duracao = ?
    WHERE id = ?""", (dur, idi))


def Atualizar():
  mus = input('Escolha a música: ')
  nvnome = input('Nova música:')
  cursor.execute("""UPDATE musicas 
      SET nome = ?
      WHERE id = ?""", (nvnome, mus))

  art = input('Novo artista: ')
  cursor.execute("""UPDATE musicas 
        SET artista = ?
        WHERE id = ?""", (art, mus))
  gen = input('Novo gênero')
  cursor.execute("""UPDATE musicas 
        SET genero = ?
        WHERE id = ?""", (gen, mus))
  dur = float(input('Nova duração: '))
  cursor.execute("""UPDATE musicas 
        SET duracao = ?
        WHERE id = ?""", (dur, mus))


#### DELETE ####
def deletar():
  var = input('Digite a música para deletar: ')
  cursor.execute("DELETE FROM musicas WHERE nome = ?", (var,))

#### SELECT #####
def buscar():
  busc = input('Qual a música que deseja buscar: ')
  cursor.execute("SELECT * FROM musicas")
  for i in cursor.fetchall():
    print(i[0])

def buscar():
  busc = input('Qual a música que deseja buscar: ')
  cursor.execute("SELECT nome = ? FROM musicas", (busc))
  for i in cursor.fetchall():
    print(i)

def Buscar():
  Busc = input('Digite o gênero que deseja buscar: ')
  cursor.execute("SELECT genero = ? FROM musicas", (Busc))
  for i in cursor.fetchall():
    print(i)

def nbuscar():
  cursor.execute("SELECT id, nome, artista, genero, duracao FROM musicas")
  for i in cursor.fetchall():
    print(i)

op = 1
while op != 0:
  print(f"""
  ### Tabela das Músicas ###
  1 - Adicionar músicas
  2 - Atualizar cadastro pelo id
  3 - Atualizar pelo nome da música
  4 - Excluir pelo nome da música
  5 - Buscar música pelo nome do artista
  6 - Buscar por gênero
  7 - Exibir músicas cadastrados
  0 - Sair do Programa
  """)
  op = int(input('Escolha sua opção:'))
  if op == 1:
    print('1')
    inserir()
    op2 = input("Deseja visualizar o cadastro? s/n")
    if op2 == "s":
      nbuscar()
  elif op == 2:
    print('2')
    atualizar()
  elif op == 3:
    print('3')
    Atualizar()
  elif op == 4:
    print('4')
    deletar()
  elif op == 5:
    print('5')
    buscar()
  elif op == 6:
    print('6')
    Buscar()
  elif op == 7:
    print('7')
    nbuscar()
  else:
    print('Fim')

conn.close()
