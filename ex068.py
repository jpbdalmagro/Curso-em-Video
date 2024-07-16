from random import randint
from time import sleep

cont = 0

print('-=' * 12, end='-')
print("\nVAMOS JOGAR PAR OU ÍMPAR")
while True:
    print('-=' * 12, end='-')
    par_ou_impar = ' '
    while par_ou_impar not in 'pi':
        par_ou_impar = str(input("\nPAR OU ÍMPAR?[P/I]")).lower().strip()
    num_p = int(input("ESCOLHA UM NÚMERO: "))
    num_c = randint(1, 10)
    print(f"Certo! Eu escolho {num_c}.")
    sleep(1)

    match par_ou_impar[0]:
        case 'p':
            if (num_p + num_c) % 2 == 0:
                print(f"Você venceu pois {num_c + num_p} é par.")
            else:
                print(f"Eu venci pois {num_c + num_p} é ímpar.")
                break
            cont += 1
        case 'i':
            if (num_p + num_c) % 2 == 1:
                print(f"Você venceu pois {num_c + num_p} é ímpar.")
            else:
                print(f"Eu venci pois {num_c + num_p} é par.")
                break
            cont += 1
    print('-=' * 12, end='-')
    sleep(.5)
    print("\nVAMOS JOGAR NOVAMENTE...")

print('-=' * 12, end='-')
print(f"\nGAME OVER! Você venceu {cont} vezes.")
