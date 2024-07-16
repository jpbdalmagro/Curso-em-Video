from time import sleep

n1 = int(input("Digite um número: "))
n2 = int(input("Digite outro número: "))
flag = 'S'
opcoes_confirmacao = [1, 2 , 3]

while flag == 'S':

    print('''O que você deseja fazer com esses números?
        [1] - SOMA
        [2] - MULTIPLICAÇÃO
        [3] - MAIOR ENTRE ELES
        [4] - ESCOLHER OUTROS NÚMEROS
        [0] - ENCERRAR SESSÃO''')
    opcao = int(input("Digite sua opção: "))

    match opcao:
        case 1:
            print(f"A soma entre {n1} e {n2} é {n1 + n2}.")
        case 2:
            print(f"O produto da multiplição dos dois numeros é {n1 * n2}.")
        case 3:
            if n1 > n2:
                print(f'{n1} é maior que {n2}.')
            elif n1 < n2:
                print(f'{n2} é maior que {n1}.')
            else:
                print("Os dois números são iguais.")
        case 4:
            print("Claro! Retornando.")
            sleep(1)
            n1 = int(input("Digite o novo número 1: "))
            n2 = int(input("Digite o novo número 2: "))
        case 0:
            print("ENCERRANDO SISTEMAS")
            sleep(1.7)
            print("Até a próxima!")
            break
        case _:
            print("VALOR INVÁLIDO")
            sleep(.5)

    if opcao in opcoes_confirmacao:
        while True:
            flag = str(input("DESEJA CONTINUAR? [S/N]:")).upper().strip()[0]
            if flag not in 'SN':
                print("OPÇÃO INVÁLIDA! TENTE NOVAMENTE")
            else:
                break
