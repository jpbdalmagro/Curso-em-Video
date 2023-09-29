from random import randint
from time import sleep

#  definindo as variaveis
empates = 0
vit_pc = 0
vit_user = 0
itens = ('PEDRA', 'PAPEL', 'TESOURA')

#  menu
print('-' * 20)
print('{:^20}'.format('VAMOS JOGAR JOKENPO'))

while True:
    print('-' * 20)
    print('''{:^20}
{:^20}
{:^20}'''.format('[0] PEDRA', '[1] PAPEL', '[2] TESOURA'))
    print('-' * 20)

    # escolhas
    computador = randint(0, 2)
    while True:
        try:
            jogador = int(input('Faça a sua escolha: '))
        except ValueError:
            print('Por favor, escolha uma opção válida.')
        else:
            if 2 >= jogador >= 0:
                break
            else:
                print('Por favor, escolha uma opção válida')

    print('\nJO')
    sleep(.5)
    print('KEN')
    sleep(.5)
    print('PO\n')

    print('-' * 20)
    print(f'''EU ESCOLHI {itens[computador]}
VOCÊ ESCOLHEU {itens[jogador]}''')
    print('-' * 20, '\n')

    match computador:
        case 0:
            match jogador:
                case 0:
                    print('Escolhemos a mesma coisa então empatamos')
                    empates += 1
                    print(f'Número de empates: {empates}.')
                case 1:
                    print(f'Você ganhou pois {itens[jogador]} vence {itens[computador]}.')
                    vit_user += 1
                    print(f'Número de vezes que você venceu: {vit_user}.')
                case 2:
                    print(f'Eu venci pois {itens[computador]} vence {itens[jogador]}.')
                    vit_pc += 1
                    print(f'Número de vezes que eu venci {vit_pc}.')
        case 1:
            match jogador:
                case 0:
                    print(f'Eu venci pois {itens[computador]} vence {itens[jogador]}.')
                    vit_pc += 1
                    print(f'Número de vezes que eu venci {vit_pc}.')
                case 1:
                    print('Escolhemos a mesma coisa então empatamos')
                    empates += 1
                    print(f'Número de empates: {empates}.')
                case 2:
                    print(f'Você ganhou pois {itens[jogador]} vence {itens[computador]}.')
                    vit_user += 1
                    print(f'Número de vezes que você venceu: {vit_user}.')
        case 2:
            match jogador:
                case 0:
                    print(f'Você ganhou pois {itens[jogador]} vence {itens[computador]}.')
                    vit_user += 1
                    print(f'Número de vezes que você venceu: {vit_user}.')
                case 1:
                    print(f'Eu venci pois {itens[computador]} vence {itens[jogador]}.')
                    vit_pc += 1
                    print(f'Número de vezes que eu venci {vit_pc}.')
                case 2:
                    print('Escolhemos a mesma coisa então empatamos')
                    empates += 1
                    print(f'Número de empates: {empates}.')

    while True:
        try:
            continuar = int(input('\nVamos jogar de novo? [1] - SIM / [0] NÃO: '))
        except ValueError:
            print('Opção Invàlida. Por favor tente novamente')
        else:
            if 1 >= continuar >= 0:
                break
            else:
                print('Opção não encontrada. Por favor tente novamente.')

    if continuar == 0:
        break

print(f'''\nO placar final ficou assim:
VOCÊ - {vit_user}
EU - {vit_pc}
EMPATES - {empates}\n''')

if vit_user > vit_pc:
    print('Você venceu o jogo.')
elif vit_user < vit_pc:
    print('Eu venci o jogo ')
else:
    print('Empatamos')

print('Vamos jogar novamente.')
