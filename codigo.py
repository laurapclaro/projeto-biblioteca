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
    nome = input("Digite o titulo oficial do livro: ")
    autor = input("Digite o nome oficial do autor da obra: ")
    ano = int(input("Digite o ano que a obra foi lançada:"))
            
    cursor.execute("""
    INSERT INTO alunos (nome, autor, ano)          
    VALUES (?, ?, ?)           
                
    """, 
    (nome, autor, ano) )



def atualizar_livros():
    conexao.commit()
print("Dados onseridos com sucesso!")



def remover_livros(id_biblioteca):
    try:
        conexao = sqlite3.connect("biblioteca.db")
        cursor = conexao.cursor()

        cursor.execute("DELETE FROM biblioteca WHERE id = ?", (id_biblioteca,))

        conexao.commit()

        if cursor.rowcount > 0:
            print("Livro removido!")
        else: 
            print("Tente novamente!")

    except Exception as erro:
        print(f"Erro ao tentar excluir livro{erro}")

    finally:
        if conexao:
            conexao.close()

deletar = int(input("Digite o id para deletar: "))
remover_livros(deletar)
