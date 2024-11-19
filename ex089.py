"""Crie um programa que leia nome e notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um
boletim contendo a média de cada um e permita que o usuário mostre as notas de cada um individualmente."""

from time import sleep

aluno = []
notas = []
boletim = []

while True:
    aluno.append(str(input("Digite o nome do Aluno: ")).capitalize())
    for i in range(0, 2):
        notas.append(float(input(f"Digite a {i + 1}ª nota: ")))
    aluno.append(notas[:])
    boletim.append(aluno[:])
    resp = str(input("Deseja continuar? [S/N]: "))
    if resp in 'Nn':
        break
    aluno.clear()
    notas.clear()
    print()

print("-" * 25)
print("ALUNO", end=' ')
print(f"{'NOME':<10}", end=' ')
print("NOTA")
for i, dado in enumerate(boletim):
    print(f"{i:^5}", end=' ')
    print(f"{dado[0]:<10}", end=' ')
    media = sum(dado[1]) / 2
    print(f"{media:.2f}")

print("-" * 25)
while True:
    consulta = int(input("Qual aluno deseja consultar? (999 encerra): "))
    if consulta == 999:

        break
    elif consulta < 0 or consulta >= len(boletim):
        print("Número inválido! Tente novemente.")
    else:
        print(f"O aluno {boletim[consulta][0]} teve as notas {boletim[consulta][1][0]} e {boletim[consulta][1][1]}.")

print("\nENCERRANDO SISTEMAS...")
sleep(3)
print("SISTEMA ENCERRADO! Tenha um bom dia!")
