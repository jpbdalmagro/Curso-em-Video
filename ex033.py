numeros = []
n = int(input('Digite um número: '))
numeros.append(n)
n = int(input('Digite outro: '))
numeros.append(n)
n = int(input('Digite um ultimo: '))
numeros.append(n)
numeros.sort()

print('O menor número digitado é {0} e o maior é {1}.'.format(numeros[0], numeros[2]))
