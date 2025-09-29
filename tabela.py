import sqlite3
conexao = sqlite3.connect("Clientes.db")

cursor = conexao.cursor()
cursor.execute("""
  CREATE TABLE IF NOT EXISTS Clientes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
               
               
               
               )              
               
               
               
               """)