import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

print("Bem-Vindo a biblioteca virtual, segue as opções de menu: ")
