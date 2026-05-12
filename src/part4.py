# ==========================================
# PARTE 4 — BUSCA SEQUENCIAL
# ==========================================

def busca_sequencial(lista, valor):

    for i in range(len(lista)):

        if lista[i] == valor:
            return i

    return -1


numeros = [10, 20, 30, 40, 50, 60]

valor = int(input("Digite o valor que deseja buscar: "))

resultado = busca_sequencial(numeros, valor)

if resultado != -1:
    print(f"Valor encontrado na posição {resultado}")
else:
    print("Valor não encontrado.")