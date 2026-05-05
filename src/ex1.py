##Versão 1
# numeros = [10, 20, 30, 40, 50]
# print(numeros)
# total = 0
# i = 0

# for i in numeros:
#     total+=i

# print(total)

##Versão 2
#numeros = [10, 20, 30, 40, 50]
#print(sum(numeros))

##Versão 3
numeros = [10, 20, 30, 40, 50]

total = 0
for i in range(len(numeros)):
    total += numeros[i]

print(total)