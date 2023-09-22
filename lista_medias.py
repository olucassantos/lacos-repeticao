print("======================================")
print("============ Média Max 3000 ==========")
print("======================================")

alunos = []
notas = []
solicita_notas = True

while solicita_notas:
    aluno = input("Digite o nome do aluno: ")
    alunos.append(aluno)

    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

    notas_aluno = (nota1, nota2, nota3)
    notas.append(notas_aluno)

    continua = input("Deseja continuar? (S/N) ")
    if continua == "N": solicita_notas = False

for aluno in alunos:
    print("Aluno: ", aluno)
    notas_aluno = notas[alunos.index(aluno)]
    quantidade_notas = len(notas_aluno)
    
    soma = 0
    for nota in notas_aluno:
        soma += nota
        print("Nota: ", nota)

    media = soma / quantidade_notas
    
    print(f"Média: %.2f" % media)
