"""Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteio() e soma_par(). A primeira
função deve sortear 5 números e colocalos na lista e a segunda função vai mostrar a soma dos valores pares sorteados."""

from random import randint
from time import sleep


def sorteio(nums: list) -> list:
    if len(nums) == 5:
        return nums

    nums.append(randint(1, 10))
    print(nums[-1], end=" ")
    sleep(.7)
    return sorteio(nums)


def soma_pares(nums: list) -> int:
    return sum(filter(lambda x: x % 2 == 0, nums))


print("Sorteando 5 valores", end=" ")
sleep(1)
numeros = sorteio(list())
sleep(1)
print("PRONTO!")

print(f"Somando os valores pares de {numeros}, obtemos {soma_pares(numeros)}.")
