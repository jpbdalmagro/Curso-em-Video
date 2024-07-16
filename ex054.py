maioridade = 0

for c in range(0,7):
    idade = int(input('Digite uma idade: '))
    if idade >= 21:
        maioridade += 1
print(f'Das 7 pessoas {maioridade} alcamçaram a maioridade.')
