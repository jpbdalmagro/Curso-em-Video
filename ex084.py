"""Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final mostre
A) Quantas pessoas foram cadastradas;
B) Uma contagem com as mais pesadas;
C) Uma contagem com as mais leves."""

cadastro = []
dados = []
pesadas = []
leves = []

while True:
    dados.append(str(input("Digite o nome: ")).strip())
    dados.append((int(input("Digite o peso em kg: "))))
    cadastro.append(dados[:])
    dados.clear()
    resp = str(input("Deseja continuar? [S/N]: "))
    if resp in 'Nn':
        break

print(f"O número de pessoas cadastradas é de {len(cadastro)}")

for i, dado in enumerate(cadastro):
    if i == 0:
        maior_peso = dado[1]
        menor_peso = dado[1]
    elif dado[1] > maior_peso:
        maior_peso = dado[1]
    elif dado[1] < menor_peso:
        menor_peso = dado[1]

for dado in cadastro:
    if maior_peso == dado[1]:
        pesadas.append(dado[0])
    if menor_peso == dado[1]:
        leves.append(dado[0])

print(f"O maior peso foi de {maior_peso}Kg de {pesadas}")
print(f"O menor peso foi de {menor_peso}Kg de {leves}")
