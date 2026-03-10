from database import conectar
from datetime import datetime

def criar_nota(usuario):
    # Solicita os dados ao usuario no terminal
    cliente = input("Cliente: ")
    # Substitui virgula por ponto para o Python entender como numero decimal
    valor_input = input("Valor: ").replace(",", ".")
    
    # Tenta converter o texto para numero float
    try:
        valor = float(valor_input)
    except ValueError:
        print("Erro: Valor invalido! Use apenas numeros.")
        return

    # Gera a data e hora atual no formato brasileiro
    data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Abre a conexao com o banco de dados
    conn = conectar()
    cursor = conn.cursor()

    # Insere os dados nas colunas especificas (o 'numero' e automatico pelo SQLite)
    cursor.execute("""
    INSERT INTO notas (cliente, valor, usuario_criacao, data_criacao)
    VALUES (?, ?, ?, ?)
    """, (cliente, valor, usuario, data))

    # Salva as alteracoes e fecha a conexao
    conn.commit()
    conn.close()
    print("Nota criada com sucesso!")

def consultar_notas():
    # Abre conexao e busca todos os registros
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM notas")
    
    # Recupera todas as linhas encontradas
    notas = cursor.fetchall()

    if not notas:
        print("Nenhuma nota cadastrada.")
        conn.close()
        return

    print("\n--- LISTA DE NOTAS ---")
    # Percorre cada nota (que vem como uma tupla/lista de valores)
    for nota in notas:
        # nota[0] e o ID/Numero (chave primaria)
        # nota[1] e o nome do Cliente
        # nota[2] e o Valor (formatado com 2 casas decimais)
        # nota[3] e o Usuario que criou
        # nota[4] e a Data/Hora
        print(
            f"Numero: {nota[0]} | "
            f"Cliente: {nota[1]} | "
            f"Valor: R$ {nota[2]:.2f} | "
            f"Usuario: {nota[3]} | "
            f"Data: {nota[4]}"
        )
    print("----------------------")
    conn.close()

def consultar_nota_por_numero():
    # Pede o ID especifico da nota
    numero = input("Digite o numero da nota: ")

    conn = conectar()
    cursor = conn.cursor()

    # Busca apenas a nota que tem o numero digitado
    cursor.execute("SELECT * FROM notas WHERE numero = ?", (numero,))
    nota = cursor.fetchone()

    # Se a nota existir (nao for None), exibe os detalhes
    if nota:
        print(
            f"Numero: {nota[0]} | "
            f"Cliente: {nota[1]} | "
            f"Valor: R$ {nota[2]:.2f} | "
            f"Data: {nota[4]}"
        )
    else:
        print("Nota nao encontrada.")

    conn.close()

def excluir_nota():
    # Pede o ID da nota para remocao
    numero = input("Numero da nota para excluir: ")

    conn = conectar()
    cursor = conn.cursor()

    # Executa o comando de delecao baseado no numero
    cursor.execute("DELETE FROM notas WHERE numero = ?", (numero,))

    # Importante: No SQLite, DELETE precisa de commit para salvar a exclusao
    conn.commit()
    conn.close()

    print("Nota removida com sucesso.")

def relatorio():
    conn = conectar()
    cursor = conn.cursor()

    # Usa funcoes de agregacao do SQL: COUNT (contar) e SUM (somar)
    cursor.execute("SELECT COUNT(*), SUM(valor) FROM notas")
    resultado = cursor.fetchone()

    # Garante que se o banco estiver vazio, o valor seja 0 em vez de None
    total_pedidos = resultado[0] if resultado[0] else 0
    soma_vendas = resultado[1] if resultado[1] else 0.0

    print("\n--- RELATORIO GERAL ---")
    print(f"Total de notas: {total_pedidos}")
    print(f"Valor total vendido: R$ {soma_vendas:.2f}")
    print("-----------------------")

    conn.close()