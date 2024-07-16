soma_idades = 0
qtd_idades = 0
mais_velho = ''
maior_idade = 0
mulheres_sub20 = 0

for c in range(0, 4):
    nome = str(input('Digite o nome: ')).strip()
    idade = int(input('Digite a idade: '))
    sexo = str(input('Digite o sexo (M/F): ')).lower()
    print('')
    soma_idades += idade
    qtd_idades += 1

    if sexo == 'm':
        if idade > maior_idade:
            maior_idade = idade
            mais_velho = nome

    if sexo == 'f':
        if idade < 20:
            mulheres_sub20 += 1

media_idades = soma_idades / qtd_idades

print(f'A média das idades é {round(media_idades, 1)}.')
print(f'O nome do homem mais velho é {mais_velho}.')
print(f'O número de mulheres com menos de 20 anos é {mulheres_sub20}.')
