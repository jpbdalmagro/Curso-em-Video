numero = 0
numeros = ('um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nome', 'dez', 'onze', 'doze', 'treze',
           'quatorze', 'quinze' 'desesseis', 'desessete', 'dezoito', 'dezenove', 'vinte')

while not 0 < numero < 21:
    numero = int(input("Digite um número de 1 a 20: "))
    if not 0 < numero < 21:
        print("Número inválido!")

print(f"Você digitou o número {numeros[numero - 1]}.")
