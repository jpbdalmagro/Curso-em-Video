"""Faça um programa que tenha uma função chamada contador(), que receba três parãmetros: início, fim e passo e realize a
contagem.
    O programa deve realizar três contagens através da função:
    a) De 1 a 10 de 1 em 1;
    b) De 10 a 0 de 2 em 2;
    c) Uma contagem personalizada."""

from time import sleep


def contagem(ini, fim, pulo):
    sleep(.35)
    if pulo == 0:
        return contagem(ini, fim, 1)
    if pulo < 0:
        return contagem(ini, fim, abs(pulo))

    if ini < fim:
        print(ini, end=" ")
        if ini + pulo > fim:
            return
        return contagem(ini + pulo, fim, pulo)
    elif ini > fim:
        print(ini, end=" ")
        if ini - pulo < fim:
            return
        return contagem(ini - pulo, fim, pulo)
    else:
        print(ini)


print("a)", end=" ")
contagem(1, 10, 1)

print("b)", end=" ")
contagem(10, 0, 2)

print("Sua vez!")
a, b, c = map(int, input("Digite o número inicial, o final e o salto separados por espaço: ").split())
print("c)", end=" ")
contagem(a, b, c)
