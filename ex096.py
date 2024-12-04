"""Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e
comprimento) e mostre a áreo do terreno"""


def area(a: float, b: float) -> float:
    return a * b


larg = float(input("Digite a largura do terreno em metros: "))
comp = float(input("Digite o comprimento do terreno em metros: "))
print(f"A área do terreno é {area(larg, comp):.2f}m²")
