identidade = []

for i in range(3):
    linha = []
    for j in range(3):
        if i == j:
            linha.append(1)
        else:
            linha.append(0)
    identidade.append(linha)

for linha in identidade:
    print(linha)
