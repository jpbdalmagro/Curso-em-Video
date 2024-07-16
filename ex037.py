numero = int(input('Digite um número inteiro: '))

print('''Para qual base você quer converter? 
[1] = Binário
[2] = Hexadecimal
[3] = Octal''')
escolha = int(input('Digite a opção escolhida: '))

match escolha:
    case 1:
        numero_alterado = bin(numero)
        base = 'BINÁRIO'
    case 2:
        numero_alterado = hex(numero)
        base = 'HEXADECIMAL'
    case 3:
        numero_alterado = oct(numero)
        base = 'OCTAL'
    case _:
        print('Função não encontrada!')
        exit()

print(f'O numero {numero} convertido em {base} é {numero_alterado [2:]}.')
