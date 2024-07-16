peso = float(input('Qual o seu peso em kg? '))
altura = int(input('Qual a sua altura em cm? '))
imc = round(peso / pow(altura / 100, 2), 2)

if imc < 18.5:
    status_imc = 'ABAIXO DO PESO'
elif imc < 25:
    status_imc = 'PESO IDEAL'
elif imc < 30:
    status_imc = 'SOBREPESO'
elif imc < 40:
    status_imc = 'OBESIDADE'
else:
    status_imc = 'OBESIDADE MÓRBIDA'

print('Seu imc é {} e seu status é {}.'.format(imc, status_imc))
