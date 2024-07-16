primo = int(input('Digite um número inteiro: '))
seletor = 0

for n in range(1, primo + 1):
    if primo % n == 0:
        seletor += 1
if seletor == 2:
    print(f'O número {primo} é primo!')
else:
    print(f'O número {primo} não é primo.')
