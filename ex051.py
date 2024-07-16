primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo_termo = primeiro_termo + (10 - 1) * razao
print('Os 10 primeiros termos são:')
for termo in range(primeiro_termo, decimo_termo + razao, razao):
    print('{} '.format(termo), end='- ')
print("FIM")
