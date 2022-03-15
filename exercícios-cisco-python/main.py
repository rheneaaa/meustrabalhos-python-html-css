from flask import Flask, render_template, request

app = Flask('app')

@app.route('/')
def index():
    return render_template('test.html')

@app.route('/hello', methods=['POST'])
def hello():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    return 'Olá %s %s, se divirta aprendendo Python <br/> <a href="/">Voltar</a>' % (first_name, last_name)

app.run(host='0.0.0.0', port=8080)