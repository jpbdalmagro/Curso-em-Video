nome = str(input('Digite seu nome completo: ')).strip()
nome = nome.split()
prinome = nome[0]
ultnome = nome[len(nome) - 1]
print('Seu primeiro nome é {}.'.format(prinome))
print('Seu ultimo nome é {}.'.format(ultnome))
