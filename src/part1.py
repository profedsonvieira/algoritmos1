# ==========================================
# PARTE 1 — MATRIZES
# ==========================================

# Criação correta da matriz 3x3
matriz = [[0 for _ in range(3)] for _ in range(3)]

# Entrada de dados
for i in range(3):
    for j in range(3):
        matriz[i][j] = int(input(f"Digite o valor para [{i}][{j}]: "))

# Exibindo matriz
print("\nMATRIZ:")
for linha in matriz:
    print(linha)

# Soma das linhas
for i in range(3):
    soma_linha = sum(matriz[i])
    print(f"Soma da linha {i+1} = {soma_linha}")

# Soma da diagonal principal
soma_diagonal = 0

for i in range(3):
    soma_diagonal += matriz[i][i]

print(f"\nSoma da diagonal principal = {soma_diagonal}")