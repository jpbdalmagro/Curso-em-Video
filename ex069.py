maior = homem = mulher_subvinte = 0

print('-' * 30)
while True:
    print("Cadastre uma pessoa")
    print('-' * 30)
    while True:
        try:
            idade = int(input("IDADE: "))
            if idade > 0:
                break
        except ValueError:
            print()
    while True:
        sexo = str(input("SEXO: [F/M] ")).strip()
        if sexo[0] in 'FfMm':
            break

    print('-' * 30)
    if idade >= 18:
        maior += 1
    if sexo[0] in 'Mm':
        homem += 1
    if sexo[0] in 'Ff' and idade < 20:
        mulher_subvinte += 1

    while True:
        resp = str(input("DESEJA CONTINUAR? [S/N] ")).strip()
        if resp in 'SsNn':
            break
    print('-' * 30)
    if resp in "Nn":
        break

print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f"Total de homens cadastrados: {homem}")
print(f"Total de mulheres com menos de 20 anos: {mulher_subvinte}")
