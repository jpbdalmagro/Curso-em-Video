"""Facça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear seis números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta."""

from random import randint
from time import sleep

jogos = []
jogo = []

print("-" * 40)
print(f"{'JOGUE NA MEGASENA':^40}")
print("-" * 40)

sorteios = int(input("Quantos jogos você quer que eu sorteie: "))
print(f"-=-{'SORTEANDO '+ str(sorteios) + ' JOGOS':^34}-=-")

for n in range(1, sorteios + 1):
    while len(jogo) <= 6:
        num = randint(1, 60)
        if num not in jogo:
            jogo.append(num)
    jogos.append(jogo[:])
    jogo.clear()

for i, j in enumerate(jogos):
    j.sort()
    sleep(.8)
    print(f"{i + 1}º jogo : {j}")

print(f"-=-{'<BOA SORTE!>':^34}-=-")
