# Importando a biblioteca do Flask para fazer um si 
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Criar lista de usuário e senha, depois vamos pegar no DB
usuarios = {
    'admin' :  'admin' ,
    'usuario' : 'senha' ,
    'Rayanna' : '1906' , 
    'Yan' : '0907' 
}

#Definindo a rota principal do site
@app.route('/')
def home():
    return render_template('index.html')

@app.route("/login1")
def login():
    return render_template('login.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route("/escolherproduto")
def escolherproduto():
    return render_template('escolherproduto.html')

@app.route("/pagamento01")
def pagamento01():
    return render_template('pagamento01.html')

@app.route("/pagamento02")
def pagamento02():
    return render_template('pagamento02.html')

@app.route("/pagamento03")
def pagamento03():
    return render_template('pagamento03.html')

@app.route("/carrinho01")
def carrinho01():
    return render_template('carrinho01.html')

# Verificar o Login
@app.route('/verificar-login' , methods=['POST'])
def verificar_login():

# Pegando o que o usuário digitou no campo de entrada de user e senha
    username = request.form['usuário']
    password = request.form['senha']

# Verifica se o usuário digitado está na lista e se a senha está certa
    if username in usuarios and usuarios[username] == password:
        return redirect(url_for("escolherproduto"))
    else:
        return "Usuário ou senha inválidos"
    
    # Parte principal do programa e Python
if __name__ == '__main__':
    app.run(debug=True)  


