"""Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai monitorar o nome e quantas
partidas ele jogou. Depoids vai ler a quantidade de gols feitos em cada partida. No final tudo será guardado em um
dicionário, incluindo o total de gols feitos durante o campeonato."""

from random import randint


def cadastro(d={}):
    d['Nome'] = str(input("Digite o nome do jogador: "))
    d['Partidas'] = int(input("Digite o número de partidas jogadas: "))
    # d['Gols'] = [int(input(f"Digite quantos gols o jogador fez na {x + 1}º partida: ")) for x in range(d["Partidas"])]
    d['Gols'] = [gols() for x in range(d["Partidas"])]
    d['Total de Gols'] = sum(d['Gols'])
    d['Media de Gols'] = round(d['Total de Gols'] / d['Partidas'], 2)
    d['Aproveitamento p/ Partida'] = str(round((len(d['Gols']) - d['Gols'].count(0)) * 100 / len(d['Gols']), 2)) + '%'

    return d


def gols():
    prob = randint(1, 44)

    if prob <= 20:
        return 0
    elif prob <= 32:
        return 1
    elif prob <= 38:
        return 2
    elif prob <= 41:
        return 3
    elif prob <= 43:
        return 4
    else:
        return 5


jogador = cadastro()

print('-=-' * 20)
print(jogador)
print('-=-' * 20)
print(f"{'Dados do jogador':^50}")
print("-" * 50)

for tipo, dado in jogador.items():
    if tipo != 'Gols':
        print(f"{tipo:<25}{dado:>25}")

print(f"Partida com mais gols{jogador['Gols'].index(max(jogador['Gols'])) + 1:>29}º")
print("-" * 50)
print('-=-' * 20)
print(f"{'RESUMO':^60}")

for i in range(len(jogador['Gols'])):
    print(f"Na {i + 1}º partida fez {jogador['Gols'][i]} gol(s).")
