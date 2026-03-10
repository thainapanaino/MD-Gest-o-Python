from menu_principal import menu
from database import criar_tabela

criar_tabela()

usuario_logado = input("Digite seu nome: ")

menu(usuario_logado)