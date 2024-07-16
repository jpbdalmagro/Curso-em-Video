num_i = num = int(input("Digite um número para descobrir seu fatorial: "))
contador = num

while contador > 1:
    num *= (contador - 1)
    contador -= 1

print("O fatorial de {} é {}".format(num_i, num))
