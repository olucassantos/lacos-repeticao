## Exercicio 4 - Lista de Médias (60 min)
# - Escreva um programa que solicita o nome de alunos e suas respectivas notas de 4 provas. Ao final o programa deve imprimir o nome dos alunos e suas médias.

# Solicitar os alunos e suas respectivas notas
# Calculas as médias
# Mostrar o nome e a média da lista de alunos

print("======================================")
print("============ Média Max 3000 ==========")
print("======================================")

alunos = []
notas = []
continua = 'S'

while continua == 'S':
    aluno = input("Informe o nome do aluno: ")

    nota1 = float(input("Informe a primeira nota: "))
    nota2 = float(input("Informe a segunda nota: "))
    nota3 = float(input("Informe a terceira nota: "))
    nota4 = float(input("Informe a quarta nota: "))

    alunos.append(aluno)
    notas.append((nota1, nota2, nota3, nota4))

    continua = input("Deseja inserir mais algum aluno (S/N)?")

# for aluno in alunos:
#     print(f"Aluno: {aluno}")

#     notas_aluno = notas[alunos.index(aluno)]
#     media = sum(notas_aluno) / len(notas_aluno)

#     print("Média: ", media)

for indice, aluno in enumerate(alunos):
    print(f'Aluno: {aluno}')
    
    notas_aluno = notas[indice]
    media = sum(notas_aluno) / len(notas_aluno)

    print("Média: ", media)