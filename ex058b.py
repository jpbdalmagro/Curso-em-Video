from random import randint
from time import sleep as slp

tentativas = 0
numero_pc = randint(1, 10)

print("Vou pensar em um número. Tente adivinhar.")
inicio = input("Pressione a tecla 'ENTER' para prosseguir.")
print("HMM")
slp(1.5)
print("PRONTO!")
while True:
    tentativas += 1
    while True:
        try:
            numero_player = int(input("Escolha um número: "))
        except ValueError:
            print("Por favor! Digite um número inteiro!")
        else:
            break
    if numero_player == numero_pc:
        break
    elif numero_player == numero_pc - 1 or numero_player == numero_pc + 1:
        print("Você passou perto. Tente novamente.")
    else:
        print("Você errou! Tente novamente.")

if tentativas == 1:
    print("UAU! Você acertou de primeira")
elif tentativas <= 5:
    print(f"Parabéns! Você levou apenas {tentativas} tentativas.")
else:
    print(f"NOSSA! Você demorou pra acertar. Levou {tentativas} tentativas, mas parabéns mesmo assim. ")
