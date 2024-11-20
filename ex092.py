"""Crie um progama que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em un dicionário
se caso a CTPS for diferente de zero, o dicionário receberá também o ano de contrartação e o salário. Calcule e
acrescente além da idadecom quantos anos a pessoa vai se aposentar."""

from datetime import datetime


def cadastro(ano: int) -> dict:
    pessoa = {}
    dados = {}

    nome = str(input("Nome: ")).strip().capitalize()
    ano_nasc = int(input("Ano de Nascimento: "))
    idade = ano - ano_nasc
    ctps = int(input("Digite a carteira de trablaho(0 para não tem): "))

    dados['Idade'] = idade
    dados['CTPS'] = ctps

    if ctps != 0:
        ano_contrato = int(input("Digite o ano da contratação: "))
        salario = float(input("Digite o salário: "))
        idade_aposentadoria = ano_contrato + 35 - ano_nasc

        dados['Ano de Contratação'] = ano_contrato
        dados['Salário'] = salario
        dados['Aposentadoria'] = idade_aposentadoria

    pessoa[nome] = dados.copy()

    return pessoa.copy()


people = cadastro(datetime.now().year)

print(people)
