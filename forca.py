from random import choice
from time import sleep

tentativas = 10
palavras = ['colher', 'carro', 'argila', 'damasco', 'estrela', 'destreza', 'feijao', 'guardanapo', 'pelugem',
            'carambola', 'paralelepipedo', 'inconstitucionalissimamente', 'papagaio', 'jabuticaba', 'ronco', 'motor',
            'aspirado', 'cassino', 'namoro', 'rapadura', 'papaleguas', 'musica', 'navegador', 'arquivo']
letras_usadas = []
letras_erradas = []
palavra_escolhida = choice(palavras)
ganhou = False

print('Vamos brincar de jogo da forca!')
print('Você terá 10 tentativas para acertar!')
print('Deixa eu pensar. . .')
sleep(1.5)
print('Pronto! A palavra escolhida é:')

while True:
    for letra in palavra_escolhida:
        if letra.lower() in letras_usadas:
            print(f'{letra} ', end='')
        else:
            print('_ ', end='')

    while True:
        letra_escolhida = input('\nEscolha uma letra: ').strip().lower()
        if letra_escolhida in letras_usadas:
            print('Essa letra já foi usada!')
        elif len(letra_escolhida) > 1:
            print('Digite UMA letra.')
        elif letra_escolhida == '':
            print('Digite uma letra')
        else:
            letras_usadas.append(letra_escolhida.lower())
            break

    if letra_escolhida in palavra_escolhida:
        print('\nVocê acertou uma letra!')
    else:
        print('\nVocê errou a letra!')
        tentativas -= 1
        print('Agora você tem {} chances.'.format(tentativas))
        letras_erradas.append(letra_escolhida)

    if letras_erradas:
        print('Essas são as letras erradas{}: \n'.format(letras_erradas))

    ganhou = True
    for letra in palavra_escolhida:
        if letra not in letras_usadas:
            ganhou = False

    if tentativas == 0 or ganhou:
        break

if ganhou:
    print(f'\nPARABÉNS! VOCÊ VENCEU! A palavra era {palavra_escolhida}')
else:
    print('Suas tentativas acabaram. A palavra era {}.'.format(palavra_escolhida))
