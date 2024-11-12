import sqlite3

# Função que conecta o banco de dados
def conectar_banco ():
    conexao = sqlite3.connect('meu_banco.db')