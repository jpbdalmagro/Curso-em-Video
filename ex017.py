from math import hypot
cato = float(input('Digite o cateto oposto: '))
cata = float(input('Digite o cateto adjacente: '))
hipotenusa = hypot(cato,cata)
print('O valor da hipotenusa é {:.2f}.'.format(hipotenusa))
