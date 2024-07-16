from random import randint


numero = randint(0, 5)
resposta = int(input('Tente adivinhar o número que estou pensando! (dica 0 a 5): '))
print('VOCÊ ACERTOU!' if numero == resposta else 'Você errou ;-;, o número era {}.'.format(numero))
