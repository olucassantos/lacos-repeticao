## Exercício 3 - Jogo de descobrir o valor (60 min)
#     - Escreva um programa que sorteia um valor de 1 a 100. O jogador pode então tentar acertar o valor, sendo que o programa informará se o chute é menor ou maior que o valor sorteado. O processo se repete até que o jogador acerte o valor sorteado.
#     - Refatore o código para ao final mostre quantas tentativas foram necessárias para acertar.

from random import randint

# Sortear um numero aleatório
# Enquanto o jogador não acertar, perguntar um palpite
# Mostrar se está maior, menor ou correto
# Mostrar a quantidade de tentativas

numero_aleatorio = randint(0, 100)
palpite = 0
tentativas = 0

while palpite != numero_aleatorio:
    palpite = int(input("Qual o seu palpite: "))
    tentativas += 1

    if palpite > numero_aleatorio:
        print("O numero sorteado é menor.")
    elif palpite < numero_aleatorio:
        print("O numero sorteado é maior.")
    else:
        print("Você acertou!")

print(f"Tentativas: {tentativas}")