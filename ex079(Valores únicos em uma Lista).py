numeros = []

while True:
    num = int(input("Digite um valor: "))
    if num in numeros:
        print(f"Resposta inválida! {num} já está na lista.")
    else:
        numeros.append(num)
        print("Número adicionado com sucesso!")
    resp = str(input("Deseja continuar? [S/N]")).strip().lower()
    if resp in 'n':
        break

numeros.sort()

print(f"Os números digitados em ordem crescente são {numeros}")
