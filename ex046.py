from time import sleep

print('Contagem regressiva!')
seg = int(input('Quantos segundos? '))

for seg in range(seg, 0, -1):
    print(seg)
    sleep(1)
print('FIM!')
