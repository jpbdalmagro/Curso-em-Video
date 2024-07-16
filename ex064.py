soma_num = num_termos = 0

num = int(input("Digite um numero [999 para sair]: "))

while num != 999:
    soma_num += num
    num_termos += 1
    num = int(input("Digite um numero [999 para sair]: "))

print(f"Você digitou {num_termos} termos e a soma deles é {soma_num}")
