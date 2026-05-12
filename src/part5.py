# ==========================================
# PARTE 5 — BUSCA BINÁRIA
# ==========================================

def busca_binaria(lista, valor):

    inicio = 0
    fim = len(lista) - 1

    comparacoes = 0

    while inicio <= fim:

        comparacoes += 1

        meio = (inicio + fim) // 2

        if lista[meio] == valor:
            return meio, comparacoes

        elif lista[meio] < valor:
            inicio = meio + 1

        else:
            fim = meio - 1

    return -1, comparacoes


lista = [5, 10, 15, 20, 25, 30, 35, 40]

valor = int(input("Digite o valor para busca binária: "))

posicao, comparacoes = busca_binaria(lista, valor)

if posicao != -1:
    print(f"\nValor encontrado na posição {posicao}")
else:
    print("\nValor não encontrado")

print(f"Quantidade de comparações: {comparacoes}")

# Explicação
print("\nEXPLICAÇÃO:")
print("A busca binária é mais eficiente porque divide")
print("a lista ao meio a cada comparação.")
print("Sua complexidade é O(log n).")