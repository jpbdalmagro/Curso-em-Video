"""Crie um progama que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em dicionário e
todos os dicionários em uma lista. No final mostre:
- Quantas pessoas foram cadastradas
- A média de idade das pessoas
- Uma lista com todas as mulheres
- Uma lista com todas as pessoas acima da idade média"""


def loop(lista):
    lista.append(cadastro())
    flag = str(input("Deseja continuar? [S/N]")).strip().lower()
    if flag == 'n':
        return lista
    else:
        return loop(lista)


def cadastro(d={}):
    d['nome'] = str(input("Digite o nome da pessoa: ")).strip().capitalize()
    d['sexo'] = str(input("Digite o sexo da pessoa: [M/F]")).strip().upper()
    d['idade'] = int(input("Digite a idade da pessoa: "))

    return d.copy()


pessoas = []
pessoas = loop(pessoas)

media = sum([pessoa['idade'] for pessoa in pessoas]) / len(pessoas)
mulheres = [pessoa['nome'] for pessoa in pessoas if pessoa['sexo'][0] == 'F']
acima_media = [pessoa for pessoa in pessoas if pessoa['idade'] > media]

print("=" * 50)
print(f"- O grupo tem {len(pessoas)} pessoa(s).")
print(f"- A média de idade do grupo é {media:.2f} anos.")

if mulheres:
    print(f"- As mulheres do grupo são ", end='')
    for m in mulheres:
        print(m, end=' ')
    print(".")

print(f"- Pessoas acima com a idade acima da média:")

for pessoa in acima_media:
    for k, v in pessoa.items():
        print(f"{k}:{v};", end=' ')
    print()
