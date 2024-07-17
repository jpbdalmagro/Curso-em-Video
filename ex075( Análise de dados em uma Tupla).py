par = False

print("Digite quatro valores.")
numeros = (int(input("Primeiro: ")),
           int(input("Segundo: ")),
           int(input("Terceiro: ")),
           int(input("Quarto: ")))

print(f"Você digitou os números {numeros}")
if numeros.count(9) > 0:
    print(f"O número de vezes que o nove aparece é {numeros.count(9)}")
else:
    print("O número 9 não aparece nenhuma vez.")

if 3 in numeros:
    print(f"A primeira vez que o 3 aparece é na posição {numeros.index(3) + 1}")
else:
    print("O número 3 não aparece nenhuma vez.")

for n in numeros:
    if n % 2 == 0:
        par = True
if par == True:
    print("Os valores pares que aparecem são ", end='')
    for n in numeros:
        if n % 2 == 0:
            print(f"{n} ", end='')
else:
    print("Não existem valores par.")
