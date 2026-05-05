lista =[]

print("Digite 5 números inteiros:")
for i in range(5):
    num = int(input(f"Número {i+1}: "))
    lista.append(num)

print("\nDobro de cada número:")
for num in lista:
    print(f"{num} x 2 = {num * 2}")
