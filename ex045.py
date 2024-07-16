from random import randint
from time import sleep as slp

placar_pc = 0
placar_jogador = 0
quebra = False


def vitoria_pc(pc, jogador):
    print('EU VENCI pois {} vence {}.'.format(pc, jogador))
    print('O placar agora está {} pra mim e {} pra você.'.format(placar_pc, placar_jogador))
    slp(1)


def vitoria_jogador(jogador, pc):
    print('VOCÊ VENCEU pois {} vence {}'.format(jogador, pc))
    print('O placar agora está {} pra mim e {} pra você.'.format(placar_pc, placar_jogador))


def empate():
    print('NOSSA! Nós escolhemos a mesma coisa, logo foi um empate!')
    print('O placar continua o mesmo {} pra mim e {} pra você.'.format(placar_pc, placar_jogador))
    slp(1)


def transforma_escolha_pc(escolha):
    if escolha == 1:
        escolha = 'pedra'
    elif escolha == 2:
        escolha = 'papel'
    else:
        escolha = 'tesoura'
    return escolha


print('-=-' * 20)
print('VAMOS JOGAR PEDRA, PAPEL E TESOURA')
print('-=-' * 20)

while True:
    print('\n HUM ', end='')
    for n in range(1, 4):
        slp(.5)
        print('. ', end='')

    slp(.5)
    escolha_pc = randint(1, 3)
    print('JÁ PENSEI! SUA VEZ...')

    while True:
        escolha_jogador = str(input('QUAL A SUA ESCOLHA? ')).strip().lower()
        if escolha_jogador == 'pedra' or escolha_jogador == 'papel' or escolha_jogador == 'tesoura':
            break
        else:
            print('EI! Esse não vale.')
    escolha_pc = transforma_escolha_pc(escolha_pc)

    if escolha_pc == escolha_jogador:
        empate()
    elif (escolha_pc == 'pedra' and escolha_jogador == 'tesoura' or escolha_pc == 'papel' and escolha_jogador == 'pedra'
          or escolha_pc == 'tesoura' and escolha_jogador == 'papel'):
        placar_pc = + 1
        vitoria_pc(escolha_pc, escolha_jogador)
    elif (escolha_jogador == 'pedra' and escolha_pc == 'tesoura' or escolha_jogador == 'papel' and escolha_pc == 'pedra'
          or escolha_jogador == 'tesoura' and escolha_pc == 'papel'):
        placar_jogador = + 1
        vitoria_jogador(escolha_jogador, escolha_pc)

    resposta = str(input('Você quer jogar de novo? ')).strip()
    while True:  # verifica se o jogador quer jogar de novo e só sai se a resposta for sim ou não
        if resposta.lower() == 'não' or resposta.lower() == 'n' or resposta.lower() == 'nao':  # se for não quebra o
            # loop
            quebra = True
            print('\033[32mOK!\033[m Foi legal jogar com você. Até mais!')
            break
        elif resposta.lower() == 'sim' or resposta.lower() == 's':  # se for sim quebra o loop
            print('\033[32mEBA!\033[m')
            break
        else:  # se a resposta for outra coisa o loop continua
            resposta = input('\033[31mNão entendi!\033[m Sim ou não? ')
            slp(0.15)

    if quebra:  # para o código se a escolha for não, se for sim repete
        break
