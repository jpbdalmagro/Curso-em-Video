numero = int(input('Digite um numero: '))
numero_e_par = numero % 2 == 0
if numero_e_par:
    print('O numero {} é par.'.format(numero))
else:
    print('O numero {} é impar.'.format(numero))
