print('ALUGUEL DE CARROS')
print('=' * 30)
print('{:^30}'.format('carros'))
print('1 - KWID')
print('2 - CIVIC')
print('3 - CAMARO')
modelo = int(input('Qual carro você utilizou? '))
print('=' * 30)

if modelo == 1:
    valorc = 60
    valorkm = 0.15
    carro = 'Kwid'
elif modelo == 2:
    valorc = 80
    valorkm = 0.25
    carro = 'Civic'
elif modelo == 3:
    valorc = 100
    valorkm = 0.35
    carro = 'Camaro'
else:
    print('Carro não encontrado! Favor tentar novamente1')
    exit()

print('Você utilizou o {}'.format(carro))
dias = int(input('Por quantos dias foi alugado? '))
km = int(input('Quantos KM foram rodados? '))
preco = (dias * valorc) + (km * valorkm)
print('O valor a se pagar pelo aluguel do {} é R${:.2f} por dia e R${:.2f} por KM rodado totalizando R${:.2f}.'.format(
    carro, valorc, valorkm, preco))
print('=' * 30)
