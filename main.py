import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS biblioteca (
       id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        autor TEXT,
        ano INTEGER 
    
)         
               

""")
print("Tabela criada!")

import os

if os.path.exists('escola.db'):
    os.remove('escola.db')
    print("Banco de dados existente excluído.")


cursor.execute("""
INSERT INTO biblioteca (nome, autor, ano) 
VALUES (?, ?, ?)        
               
               """,
("Harry Potter", "J.K Rowling", 1997)
)

conexao.commit()
conexao.close()


