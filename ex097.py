"""Faça um programa que tenha um função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
mensagem com tamanho adaptável."""


def escreva(txt):
    tamanho = len(txt)
    print("~" * (tamanho + 2))
    print(txt.center(tamanho + 2))
    print("~" * (tamanho + 2))


escreva(input("Digite uma mensagem: "))
