import streamlit
import funcoes

streamlit.title("Cadastro de clientes: ")
nome = streamlit.text_input("Digite seu nome completo: ")
telefone = streamlit.text_input("Digite seu telefone completo: ")
email = streamlit.text_input("Digite seu nome email: ")


if streamlit.button("Adicionar cliente"):
    funcoes.insereDados(nome, telefone, email)
    streamlit.success("Cliente adicionado")

