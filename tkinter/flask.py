from flask import Flask

app = Flask(__name__)

# criar a 1° pagina do site
# route -> hashtagtreinamentos.com/
# funcao -> o que você quer exibie naquela pagina
@app.route("/")
def homepage():
    return "Esse é o meu 1° site"

# colocar o site no ar
app.run()
