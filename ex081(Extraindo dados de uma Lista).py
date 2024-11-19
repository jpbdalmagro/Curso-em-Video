numeros = []

while True:
    numeros.append(int(input("Digite um número: ")))
    while True:
        flag = str(input("Deseja continuar? [S/N]: ")).strip().lower()
        if flag in 'sn' and flag != '':
            break
        if flag not in 'sn' or flag == '':
            print("Comando não reconhecido!")
    if flag == 'n':
        break

numeros.sort(reverse=True)

print(f"Você digitou {len(numeros)} elementos."
      f"\nOs números em ordem decrescente são {numeros}.")
print("O valor 5 foi encontrado." if 5 in numeros else "Valor 5 não encontrado.")