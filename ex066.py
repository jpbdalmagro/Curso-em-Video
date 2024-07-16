numeros =[]

while True:
    num = int(input("Digite um número [999 - SAIR]: "))
    if num == 999:
        break
    numeros.append(num)

print(f"Você digitou {len(numeros)}, e soma deles é {sum(numeros)}.")
