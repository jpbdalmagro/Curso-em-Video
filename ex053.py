frase = str(input('Digite uma palavra ou frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

print(f'A palavra {junto} ao contrário é {inverso}.')
if junto == inverso:
    print('E isso é um palindromo')
else:
    print('E isso não é um palindromo')
