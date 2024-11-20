"""Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da esturtura na tela"""

infos = {}

nome = str(input("Digite o nome do aluno: ")).strip().capitalize()
media = float(input(f"Digite a média de {nome}: "))

if media >= 7:
    status = "APROVADO"
elif media >= 5:
    status = "EXAME"
else:
    status = "REPROVADO"

infos['Nome'] = nome
infos['Média'] = media
infos["Situação"] = status

print("-" * 40)
for tipo, info in infos.items():
    print(f"{tipo:<20}{info:>20}")
print("-" * 40)
