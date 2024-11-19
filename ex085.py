"""Crie um programa no qual o usuário possa digitar 7 valores númericos e cadastre-os em um lista única que mantenha
separados os valores pares e ímpares. No final, mostre os valores em ordem crescente."""
numeros = [[], []]

for i in range(1, 8):
    num = int(input(f"Digite o {i}º número: "))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)

numeros[0] = list(set(numeros[0]))
numeros[1] = list(set(numeros[1]))

numeros[0].sort()
numeros[1].sort()

print(f"Valores pares digitados {numeros[0]}.")
print(f"Valores ímpares digitados {numeros[1]}.")
