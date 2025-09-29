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

# LISTANDO LIVROS
def listar_livros():
    cursor.execute("SELECT * FROM biblioteca")
    livros = cursor.fetchall()

    if not livros:
        print("Nenhum livro cadastrado.")
    else:
        print("\nLista de Livros:")
        for livro in livros:
            print(f"ID: {livro[0]} | Título: {livro[1]} | Autor: {livro[2]} | Ano: {livro[3]}")

# ADICIONANDO LIVROS
def adicionar_livros():
    nome = input("Digite o titulo oficial do livro: ")
    autor = input("Digite o nome oficial do autor da obra: ")
    ano = int(input("Digite o ano que a obra foi lançada: "))
            
    # Corrigido: inserir na tabela 'livros' (antes 'alunos')
    cursor.execute("""
    INSERT INTO biblioteca (nome, autor, ano)          
    VALUES (?, ?, ?)           
    """, (nome, autor, ano) )
    conexao.commit()  # faltava o commit para salvar

# ATUALIZANDO LIVROS
def atualizar_livros():
    # Função incompleta, adiciono um exemplo simples
    listar_livros()
    id_livro = int(input("Digite o ID do livro que deseja atualizar: "))
    novo_nome = input("Novo título do livro: ")
    novo_autor = input("Novo autor do livro: ")
    novo_ano = int(input("Novo ano de lançamento: "))
    
    cursor.execute("""
    UPDATE biblioteca SET nome = ?, autor = ?, ano = ? WHERE id = ?
    """, (novo_nome, novo_autor, novo_ano, id_livro))
    conexao.commit()
    print("Dados atualizados com sucesso!")

# REMOVENDO LIVROS
def remover_livros():
    listar_livros()
    id_biblioteca = int(input("Digite o ID do livro para deletar: "))
    try:
        
        cursor.execute("DELETE FROM biblioteca WHERE id = ?", (id_biblioteca,))
        conexao.commit()

        if cursor.rowcount > 0:
            print("Livro removido!")
        else: 
            print("ID não encontrado, tente novamente!")

    except Exception as erro:
        print(f"Erro ao tentar excluir livro: {erro}")

def sair_menu():
    print("Obrigado pela visita!!")
    conexao.close()
    exit()

# MENU INTERATIVO
print("Bem-vindo ao nosso sistema!")

while True:
    menu()
    try:
        opcao = int(input("Digite uma opção do menu: "))
    except ValueError:
        print("Por favor, digite um número válido!")
        continue

    if opcao == 1:
        listar_livros()

    elif opcao == 2:
        adicionar_livros()

    elif opcao == 3:
        atualizar_livros()

    elif opcao == 4:
        remover_livros()
     
    elif opcao == 5:
        sair_menu()

    else:
        print("Opção inválida!")