while True:
    num = int(input("Digite um número inteiro positivo: "))
    if num >= 0:
        break
    print("Número inválido! Digite um valor positivo.")

print(f"\nTabuada do {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")
