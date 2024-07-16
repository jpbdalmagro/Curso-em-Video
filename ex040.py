from statistics import mean

notas = []
quantidade_notas = int(input('Quantas notas irá computar? '))

for nota in range(1, quantidade_notas + 1):
    nota_atual = float(input('Digite a {}° nota: '.format(nota)))
    while True:
        if nota_atual > 10:
            nota_atual = int(input('A nota não deve superar 10. Tente novamente: '))
        else:
            notas.append(nota_atual)
            break

media = mean(notas)
print('A média do aluno é \033[34m{:.1f}\033[m, com isso ele está '.format(media), end='')

if media >= 7:
    print('\033[32mAPROVADO\033[m!')
elif media < 5:
    print('\033[31mREPROVADO\033[m!')
else:
    print('\033[33mEM RECUPERAÇÃO\033[m!')
