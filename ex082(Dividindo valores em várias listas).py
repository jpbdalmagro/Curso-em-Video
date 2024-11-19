numeros = []
pares = []
impares = []
flag = cont = True
i = 0

while flag:
    num = int(input("Digite um número: "))
    numeros.append(num)
    while cont:
        resp = str(input("Deseja continuar? ")).strip().lower()
        if resp == '' or resp not in 'sn':
            print("Comando não reconhecido. Tente novamente!")
        elif resp in 'sn':
            cont = False
    if resp in 'n':
        flag = False
    else:
        cont = True

while i < len(numeros):
    if numeros[i] % 2 == 0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])
    i += 1
print(numeros)
print(pares)
print(impares)
