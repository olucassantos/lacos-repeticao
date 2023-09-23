# ## Exercício 2 - Tabuada (30 min)
#     - Escreva o código para imprimir a tabuada do 2 usando um laço for.
#     - Refatore o código para solicitar ao usuário qual tabuada deve ser impressa.

maximo = int(input("Qual o numero máximo: "))
ordem = input("Qual a ordem que deseja imprimir o numeros (C/D): ")

if ordem == 'C':
    for numero in range(1, maximo + 1):
        print(numero)
elif ordem == 'D':
    for numero in range(maximo, 0, -1):
        print(numero)
else:
    print("Odem Inválida!")

if ordem == 'C':
    numero = 1
    while numero <= maximo:
        print(numero)
        numero += 1

elif ordem == 'D':
    while maximo > 0:
        print(maximo)
        maximo -= 1
else:
    print("Ordem inválida")