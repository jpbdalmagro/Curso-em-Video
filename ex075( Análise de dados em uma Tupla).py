cont_par = cont_nove = 0
verifica_tres = False

print("Digite quatro valores.")
primeiro = int(input("Primeiro: "))
segundo = int(input("Segundo: "))
terceiro = int(input("Terceiro: "))
quarto = int(input("Quarto: "))

numeros = (primeiro, segundo, terceiro, quarto)
for n in numeros:
    if n == 9:
        cont_nove += 1
    if n == 3:
        verifica_tres = True
    if n % 2 == 0:
        cont_par += 1

if not cont_nove == 0:
    print(f"O número de vezes que o nove aparece é: {cont_nove}")
else:
    print("O número 9 não aparece nenhuma vez.")

if verifica_tres is True:
    print(f"A primeira vez que o 3 aparece é na posição {numeros.index(3) + 1}")
else:
    print("O número 3 não aparece nenhuma vez.")

if not cont_par == 0:
    print(f"O número de valores pares que aparecem é {cont_par}.")
else:
    print("Nenhum valor par foi digitado.")
