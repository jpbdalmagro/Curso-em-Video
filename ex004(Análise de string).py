var = input('Digite algo: ')
print('Tipo: {}'.format(type(var)))
print('É numerico? ', var.isnumeric())
print('É alfabetico? ', var.isalpha())
print('É alfanumerico?', var.isalnum())
print(var.isspace())
print('Está em maiusculas? ', var.isupper())
print('Está em minusculas? {}'.format(var.islower()))
print('Está capitalizada? {}'.format(var.istitle()))
