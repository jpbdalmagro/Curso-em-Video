from random import randint

acertou = False
tentativas = 0
contador = 0
numeros_escolhidos = []

print("Pense em um número de 1 a 10 que vou tentar adivinhar!")
inicio = input("Pressione a tecla 'ENTER' para prosseguir.")

while not acertou:
    tentativas += 1
    numero = randint(1, 10)
    while numero in numeros_escolhidos:
        numero = randint(1, 10)
    print(f"Eu pensei no {numero}!")
    acerto = str(input("Acertei? [S/N]")).upper().strip()
    contador += 1
    if acerto[0] == 'S':
        acertou = True
    else:
        numeros_escolhidos.append(numero)
    if contador == 10:
        tentativas = 0
        break

if tentativas == 0:
    print('EI! Você está roubando. Eu já falei todos os números entre 1 e 10.')
elif tentativas == 1:
    print("OBA! E eu só precisei de uma tentativa!")
else:
    print(f"OBA! Eu precisei de {tentativas} tentativas pra acertar!")
