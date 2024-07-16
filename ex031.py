kms = int(input('Quantos kms tem a viagem? '))
print('O preço da passagem será R${:.2f}.'.format(kms * .50) if kms <= 200 else 'O preço da passagem será R${:.2f}.'
      .format(kms * .45))
