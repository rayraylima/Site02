# Importando a biblioteca do Flask para fazer um si 
from flask import Flask, render_template, request

app = Flask(__name__)

#Definindo a rota principal do site
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login1")
def login():
    return render_template('login.html')

@app.route("/escolherproduto")
def escolherproduto():
    return render_template('escolherproduto.html')

@app.route("/pagamento01")
def pagamento01():
    return render_template('pagamento01')

@app.route("/pagamento02")
def pagamento02():
    return render_template('pagamento02')

@app.route("/pagamento03")
def pagamento03():
    return render_template('pagamento03')
# Parte principal do programa e Python
if __name__ == '__main__':
    app.run(debug=True)


