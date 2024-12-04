"""Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
    O programa  tem que analisar todos os valores e dizer qual é maior."""

from time import sleep


def maior(*num):
    sleep(1)
    print("-=" * 20)
    print("Analisando os valores passados")
    sleep(1)
    if num:
        for n in num:
            print(n, end=" ")
            sleep(.5)
    print(f"Foram passados {len(num)} valores.")
    sleep(1)
    if num:
        print(f"O maior valor passado foi {max(num)}")


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
