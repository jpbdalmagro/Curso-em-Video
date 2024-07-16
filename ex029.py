velocidade = int(input('Digite uma velocidade: '))
print('O limite da via é 80km/h e o condutor que ultrapassar receberá uma multa de R$7,00 para cada km/h a mais.')
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Sua velocidade foi de {}km/h, {}km/h a mais que o permitido.'.format(velocidade, velocidade - 80))
    print('Você deverá pagar uma multa de R${:.2f}.'.format(float(multa)))
else:
    print('Sua velocidade está dentro permitido, continue assim :).')
