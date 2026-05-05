print("Preencha a Matriz A (2x2):")
A = []
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"A[{i}][{j}]: "))
        linha.append(valor)
    A.append(linha)

print("\nPreencha a Matriz B (2x2):")
B = []
for i in range(2):
    linha = []
    for j in range(2):
        valor = int(input(f"B[{i}][{j}]: "))
        linha.append(valor)
    B.append(linha)

# Calculando a soma
soma = []
for i in range(2):
    linha_soma = []
    for j in range(2):
        linha_soma.append(A[i][j] + B[i][j])
    soma.append(linha_soma)

# Exibindo os resultados
print("\nMatriz A:")
for linha in A:
    print(linha)

print("\nMatriz B:")
for linha in B:
    print(linha)

print("\nSoma das matrizes (A + B):")
for linha in soma:
    print(linha)
