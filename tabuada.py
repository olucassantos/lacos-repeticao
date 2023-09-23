# Tabuada de acordo com um numero solicitado ao usuário
tabuada = int(input("Qual tabuada deseja: "))

for numero in range(0, 11):
    print(f'{tabuada} x {numero} = {numero * tabuada}')
    