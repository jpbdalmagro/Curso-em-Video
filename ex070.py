barato = mil = total = 0
nome_barato = ''

print('-' * 30)

while True:
    nome = str(input("Digete o nome de um produto: ")).strip().capitalize()
    valor = float(input("Digite o valor desse produto: R$"))

    if barato == 0 or valor < barato:
        barato = valor
        nome_barato = nome
    if valor > 1000:
        mil += 1
    total += valor
    continuar = 'A'
    while continuar[0] not in 'SsNn':
        continuar = str(input("Deseja continuar inserindo valores? [S/N] "))

    print('-' * 30)
    if continuar[0] in "nN":
        break

print(f"\nO preço total da compra foi R${total:.2f}."
      f"\nTemos {mil} produtos passando de R$1000.00"
      f"\nO produto mais barato foi {nome_barato} custando R${barato:.2f}.")
