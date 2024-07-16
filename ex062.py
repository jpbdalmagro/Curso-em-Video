primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
n_termos = int(input("Digite quantos termos você gostaria de ver: "))
enesio_termo = primeiro_termo + (n_termos - 1) * razao
termo = primeiro_termo
print(f'Os {n_termos} são termos são:')

while n_termos > 0:
    while termo <= enesio_termo:
        print('{} '.format(termo), end='- ')
        termo += razao
    n_termos = int(input("Digite quantos termos gostaria de ver a seguir: "))
    if n_termos > 0:
        print(f"Os próximos {n_termos} são:")
        enesio_termo = termo + (n_termos - 1) * razao


print("FIM!")
