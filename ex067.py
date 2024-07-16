while True:
    num = int(input("Qual número você deseja ver a tabuada: "))
    if num < 0:
        break
    print("{:-^20}".format("Tabuada do " + str(num)))
    for n in range(1, 11):
        linha = f"{num} x {n:2} = {num * n:2}"
        print(f'{linha:^20}')
    print('-' * 20)

print('-' * 20)
print("{:^20}".format("PROCESSO ENCERRADO"))
