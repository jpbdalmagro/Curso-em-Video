print("SEQUENCIA DE FIBONACCI")
n1 = 0
n2 = 1
n3 = 0
contador = 0
num = int(input("Digite quantos números da sequencia de fibonacci você deseja ver: "))

print(f"{n1} ", end='- ')
print(f"{n2} ", end='- ')

while contador <= num - 3:
    n3 = n2 + n1
    print(f"{n3} ", end='- ')
    n1 = n2
    n2 = n3
    contador += 1
print("FIM")
