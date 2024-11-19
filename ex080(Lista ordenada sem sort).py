numeros = []

for i in range(0, 5):
    num = int(input("Digite um valor: "))
    if not numeros:
        numeros.append(num)
        print("Adicionado na 1ª posição.")
    else:
        for c, n in enumerate(numeros):
            if num < n:
                numeros.insert(c, num)
                print(f"Adicionado na {c + 1}ª posição.")
                break
            if num > numeros[-1]:
                numeros.append(num)
                print("Adicionado na última posição.")
                break

print(f"Os números em ordem crescente são {numeros}")
