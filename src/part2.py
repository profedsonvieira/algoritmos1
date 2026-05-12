# ==========================================
# PARTE 2 — CÓPIA RASA VS PROFUNDA
# ==========================================

import copy

matriz = [[1, 2], [3, 4]]

# Cópia rasa
copia_rasa = matriz.copy()

# Cópia profunda
copia_profunda = copy.deepcopy(matriz)

# Alterando a cópia rasa
copia_rasa[0][0] = 99

print("Matriz original:")
print(matriz)

print("\nCópia rasa:")
print(copia_rasa)

print("\nCópia profunda:")
print(copia_profunda)

# Explicação
print("\nEXPLICAÇÃO:")
print("A matriz original foi alterada porque a cópia rasa")
print("mantém referências para as listas internas.")
print("A cópia profunda cria objetos totalmente independentes.")