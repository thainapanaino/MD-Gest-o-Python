from notas import (
    criar_nota,
    consultar_notas,
    consultar_nota_por_numero,
    excluir_nota,
    relatorio
)

def menu(usuario):
    while True:
        print('\n1 - Criar nota')
        print('2 - Mostrar todas')
        print('3 - Buscar por número')
        print('4 - Excluir nota')
        print('5 - Relatório')
        print('0 - Sair')

        opcao = input('Escolha: ')

        if opcao == '1':
            criar_nota(usuario)
        elif opcao == '2':
            consultar_notas()
        elif opcao == '3':
            consultar_nota_por_numero()
        elif opcao == '4':
            excluir_nota()
        elif opcao == '5':
            relatorio()
        elif opcao == '0':
            print('Saindo...')
            break
        else:
            print('Opção inválida')