# ==========================================
# DESAFIO EXTRA
# ==========================================

alunos = []

quantidade = int(input("Quantos alunos deseja cadastrar? "))

for i in range(quantidade):

    nome = input("Nome do aluno: ")
    nota = float(input("Nota do aluno: "))

    aluno = {
        "nome": nome,
        "nota": nota
    }

    alunos.append(aluno)

# Ordenando por nota
alunos_ordenados = sorted(alunos, key=lambda x: x["nota"])

print("\nALUNOS ORDENADOS POR NOTA:")

for aluno in alunos_ordenados:
    print(f'{aluno["nome"]} - {aluno["nota"]}')

# Busca por nome
busca = input("\nDigite o nome do aluno para buscar: ")

encontrado = False

for aluno in alunos:

    if aluno["nome"].lower() == busca.lower():

        print("\nAluno encontrado:")
        print(f'Nome: {aluno["nome"]}')
        print(f'Nota: {aluno["nota"]}')

        encontrado = True

if not encontrado:
    print("Aluno não encontrado.")