from flask import Flask, render_template, request
app = Flask('app')
import sqlite3
banco = "database.db"

conexao = sqlite3.connect(banco, check_same_thread=False)
cursor = conexao.cursor()

# criar tabela
criar_tabela = """ CREATE TABLE IF NOT EXISTS professores (
                        id integer PRIMARY KEY AUTOINCREMENT,
                        nome text,
                        sobrenome text
                      ); """
cursor.execute(criar_tabela)

def inserir(t1, t2):
  cursor = conexao.cursor()
  nome = t1
  sobrenome = t2
  cursor.execute("INSERT INTO professores (nome, sobrenome) VALUES (?,?)", (nome, sobrenome))
  conexao.commit()

def pesquisar(v1):
  cursor = conexao.cursor()
  sobre = v1
  cursor.execute("SELECT * FROM professores WHERE nome = ?", (sobre,))
  result = cursor.fetchall()
  print(result)
  return '''
    for i in result:
    print(i)
  '''
  
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/cadastro', methods=['POST'])
def cadastro():
  first_name = request.form['nome']
  last_name = request.form['sobrenome']
  inserir(first_name, last_name)
  return 'Cadastro de %s %s realizado com sucesso! <br/> <a href="/">Voltar</a>' % (first_name, last_name)

@app.route('/consulta', methods=['POST'])
def consulta():
  first_name = request.form['nome']
  pesquisar(first_name)
#  resultado()
  return '<a href="/">Voltar</a>'

app.run(host='0.0.0.0', port=8080)
conexao.close()