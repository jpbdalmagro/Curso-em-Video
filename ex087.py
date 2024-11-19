"""Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados;
B) A soma dos valores da terceira coluna;
C) O maior valor da segunda linha."""

matriz = [[[], [], []], [[], [], []], [[], [], []]]
soma_par = soma_col = maior = 0

for r in range(0, 3):
    for c in range(0, 3):
        num = int(input(f"Digite um valor para a posiação [{r},{c}]: "))
        matriz[r][c].append(num)
        if num % 2 == 0:
            soma_par += num

for r in matriz:
    for c in r:
        if r.index(c) == 2:
            soma_col += c[0]
        if matriz.index(r) == 1:
            if c[0] > maior:
                maior = c[0]
        print(c, end='')
    print()

print(f"A soma dos valores pares é {soma_par}.")
print(f"A soma da terceira coluna é {soma_col}.")
print(f"O maior valor da segunda linha é {maior}.")
