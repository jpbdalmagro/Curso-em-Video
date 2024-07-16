from time import sleep

n = int(input('Digite um número para ver sua tabuada: '))
print('PROCESSANDO. . .')
sleep(3)

print('-' * 12)
for tab in range(1, 11):
    print('{} x {:2} = {}'.format(n, tab, n * tab))
print('-' * 12)
