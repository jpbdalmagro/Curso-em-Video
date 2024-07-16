primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
termo = primeiro_termo
print('Os 10 primeiros termos são:')

while termo <= decimo_termo:
    print('{} '.format(termo), end='- ')
    termo += razao
print("FIM")
