sexo = str(input("Digite seu sexo. Por favor utilize somente M ou F: ")).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input("INFORMAÇÃO INVÁLIDA! Por favor utilize somente M ou F: ")).strip().upper()[0]

print("Sexo válido")
