import sqlite3

conexao = sqlite3.connect("biblioteca.db")
cursor = conexao.cursor()

("""
CREATE TABLE IF NOT EXISTS biblioteca(
    id INTERGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    autor TEXT NOT NULL,
    ano INTERGER)
 """)
print("Tabela criada!")

