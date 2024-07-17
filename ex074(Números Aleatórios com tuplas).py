from random import randint

numeros = (randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9), randint(1, 9))

print("Os Números sorteados são: ", end='' )
for numero in numeros:
    print(numero, end=' ')

print(f"\nO maior valor sorteado foi {max(numeros)}")
print(f"O menor valor sorteado foi {min(numeros)}")
