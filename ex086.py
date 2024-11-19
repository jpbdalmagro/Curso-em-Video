"""Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lidos pelo teclado. No final mostre a
matriz na tela, com formatação correta."""

matriz = [[[], [], []], [[], [], []], [[], [], []]]

for i in range(0, 3):
    for c in range(0, 3):
        matriz[i][c].append(int(input(f"Digite um valor para a posiação [{i},{c}]: ")))

for line in matriz:
    for c in line:
        print(c, end='')
    print()
