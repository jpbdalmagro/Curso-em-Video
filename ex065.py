flag = 'S'
numeros = []
maior = 0
menor = 0

while flag[0] in 'Ss':
    numero = int(input("Digite um numero: "))
    numeros.append(numero)

    if len(numeros) == 1:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

    flag = str(input("Deseja continuar? [S/N]: ")).upper().strip()

soma = sum(numeros)
qtd = len(numeros)

print(f"Você digitou {qtd} termos e a soma deles é {soma}")
print(f"A média dos números digitados é {round(soma / qtd, 2)}, o maior termo digitado foi {maior} e o menor {menor}.")
