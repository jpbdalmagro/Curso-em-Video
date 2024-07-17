numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nome', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze' 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        numero = int(input("Digite um número de 1 a 20: "))
        if 0 < numero <= 20:
            break
        print("Número inválido!")

    print(f"Você digitou o número {numeros[numero - 1]}.")
    while True:
        flag = str(input("Quer continuar? ")).strip().lower()[0]
        if flag in 'sny':
            break
        print("Não entendi.")
    if flag in 'n':
        break

print("Até mais!")
