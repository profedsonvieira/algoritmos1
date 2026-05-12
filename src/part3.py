# ==========================================
# PARTE 3 — ORDENAÇÃO
# ==========================================

import random

# Gerando lista aleatória
lista = [random.randint(1, 100) for _ in range(10)]

print("Lista original:")
print(lista)

# sort() altera a lista original
lista_sort = lista.copy()

lista_sort.sort()

print("\nUsando sort():")
print(lista_sort)

# sorted() cria nova lista
nova_lista = sorted(lista)

print("\nUsando sorted():")
print(nova_lista)

print("\nLista original após sorted():")
print(lista)

# Explicação
print("\nDIFERENÇA:")
print("sort() modifica a lista original.")
print("sorted() cria uma nova lista ordenada.")