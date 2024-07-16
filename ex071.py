cinquenta = vinte = dez = um = 0
valor = int(input("Digite quanto você quer sacar: R$"))

while valor - 50 >= 0:
    valor -= 50
    cinquenta += 1
while valor - 20 >= 0:
    valor -= 20
    vinte += 1
while valor - 10 >= 0:
    valor -= 10
    dez += 1
while valor - 1 >= 0:
    valor -= 1
    um += 1
print(f"TOTAL DE {cinquenta} CÉDULAS DE R$50"
      f"\nTOTAL DE {vinte} CÉDULAS DE R$20"
      f"\nTOTAL DE {dez} CÉDULAS DE R$10"
      f"\nTOTAL DE {um} cÉDULAS DE R$1.")
