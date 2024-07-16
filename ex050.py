soma = 0

for c in range(0, 6):
    n = int(input('Digite um numero: '))
    if n % 2 == 0:
        soma += n
print(f'A soma entre os números pares digitados é {soma}.')
