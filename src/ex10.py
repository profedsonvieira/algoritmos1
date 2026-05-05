lista_a = [1, 2, 3]
lista_b = lista_a
lista_b.append(4)
print(lista_a)

# Resposta 10 – Testando referências em listas (mutabilidade)
# 1. O que será exibido no print(lista_a)?
# text
# [1, 2, 3, 4]
# 2. Explicação:
# Isso acontece porque, em Python, quando fazemos lista_b = lista_a, não estamos criando uma nova lista. Estamos apenas fazendo com que lista_b aponte para o mesmo objeto que lista_a já aponta. Ambas as variáveis referenciam o mesmo endereço de memória.
# Portanto, qualquer alteração feita através de lista_b (como append(4)) afeta diretamente o objeto que lista_a também está vendo. Esse comportamento ocorre porque listas são mutáveis em Python.
# 3. Como fazer uma cópia independente?
# Existem três formas comuns:
# python
# # Forma 1: usando o método copy()
# lista_b = lista_a.copy()

# # Forma 2: usando o construtor list()
# lista_b = list(lista_a)

# # Forma 3: usando fatiamento
# lista_b = lista_a[:]
# Exemplo correto:
# python
# lista_a = [1, 2, 3]
# lista_b = lista_a.copy()  # cópia independente
# lista_b.append(4)
# print(lista_a)  # [1, 2, 3]  (não foi alterada)
# print(lista_b)  # [1, 2, 3, 4]
