from datetime import datetime

notas = []

def criar_nota(usuario):
    valor = input("Valor da nota: ")

    valor = valor.replace(',', '.')

    try:
        valor = float(valor)
    except ValueError:
        print("Erro: valor deve ser numérico.")
        return

    # Geração automática do número
    if not notas:
        numero = "1"
    else:
        ultimo_numero = int(notas[-1]["numero"])
        numero = str(ultimo_numero + 1)

    nota = {
        "numero": numero,
        "valor": valor,
        "data_criacao": datetime.now(),
        "usuario_criacao": usuario
    }

    notas.append(nota)
    print(f"Nota {numero} criada com sucesso!")


def consultar_notas():
    if not notas:
        print("Nenhuma nota cadastrada.")
        return

    print("Notas cadastradas:")
    for i, nota in enumerate(notas, start=1):
        print(
            f"{i}. Número: {nota['numero']} | "
            f"Valor: {nota['valor']} | "
            f"Criada por: {nota['usuario_criacao']} | "
            f"Em: {nota['data_criacao'].strftime('%d/%m/%Y %H:%M')}"
        )

def consultar_nota_por_numero():
    numero = input("Digite o número da nota: ")

    for nota in notas:
        if nota["numero"] == numero:
            print(
                f"Número: {nota['numero']} | "
                f"Valor: {nota['valor']} | "
                f"Criada por: {nota['usuario_criacao']} | "
                f"Em: {nota['data_criacao'].strftime('%d/%m/%Y %H:%M')}"
            )
            return

    print("Nota não encontrada.")


def excluir_nota():
    numero = input("Digite o número da nota para excluir: ")

    for nota in notas:
        if nota["numero"] == numero:
            notas.remove(nota)
            print("Nota removida com sucesso.")
            return

    print("Nota não encontrada.")


def relatorio():
    if not notas:
        print("Nenhuma nota cadastrada.")
        return

    total = sum(nota["valor"] for nota in notas)
    print(f"Total de notas: {len(notas)}")
    print(f"Valor total: {total}")