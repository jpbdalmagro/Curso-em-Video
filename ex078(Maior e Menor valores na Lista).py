numeros = []

for i in range(0, 5):
    numeros.append(int(input(f"Digite o {i + 1}º número: ")))


print(f"Os números digitados foram {numeros}.")
numeros.sort()
print(f"O maior número digitado foi {numeros[-1]}.")
print(f"O menor número foi {numeros[0]}.")
