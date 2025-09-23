import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

def menu():
    print("\nMenu Livros")
    print("1 - Listar livros")
    print("2 - Adicionar livro")
    print("3 - Atualizar livro")
    print("4 - Remover livro")
    print("5 - Sair")


def listar_livros():
    cursor.execute("SELECT * FROM livros")
    livros = cursor.fetchall()

    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("\nLista de Livros:")
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]}")

def adicionar_livros():
    