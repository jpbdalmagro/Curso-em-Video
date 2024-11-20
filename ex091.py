"""Cire um programa onde 4 jogadores jogam um dado e tenham resultados aleatórios. Guarde esses resultados em um
dicionário. No final coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número."""

from random import randint
from time import sleep


def gera_nums(i: int) -> int:
    num = randint(1, 6)
    print(f"O jogador {i} tirou {num}")
    sleep(1)
    return num


def add_dict(i: int):
    if i > 3:
        return
    else:
        idd = 'Jogador ' + str(i + 1)
        sorteio[idd] = nums[i]
        return add_dict(i + 1)


nums = [gera_nums(x + 1) for x in range(4)]

sorteio = {}
add_dict(0)
sorteio = dict(sorted(sorteio.items(), key=lambda item: item[1], reverse=True))

pos = 1

for p, v in sorteio.items():
    print(f"{pos}º {p} com {v}")
    pos += 1
