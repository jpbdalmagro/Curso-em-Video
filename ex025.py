nome = input('Digite um nome: ')
verifica_nome = 'silva' in nome.lower()
if verifica_nome:
    print('Seu nome contém "Silva".')
else:
    print('Seu nome não contém "Silva".')
