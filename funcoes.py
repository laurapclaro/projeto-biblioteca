import sqlite3
def connectaBD():
    conexao = sqlite3.connect("Clientes.db")
    return conexao


def insereDados(nome, telefone, email):
    conexao = connectaBD()
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO Clientes(nome, telefone, email) VALUES (?, ?, ?)", (nome, telefone, email))
    conexao.commit()
    conexao.close()


def listarDados():
    conexao = connectaBD()
    cursor = conexao.cursor()
    cursor.execute("SELECT  * FROM Clientes ")
    dados = cursor.fetchall()
    cursor.close()
    return dados