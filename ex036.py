valor_casa = float(input('Qual o valor da casa? R$'))
anos = int(input('Em quantos quantos anos planeja pagar? '))
salario = float(input('Qual o seu salário? R$'))
meses = anos * 12
prestacoes = valor_casa / meses
trinta_porcento_salario = salario * 30 / 100

print('Serão {} prestações de R${:.2f} cada.'.format(meses, prestacoes))
if prestacoes < trinta_porcento_salario:
    print('\033[32mAPROVADO!\033[32m')
    print('Você pode fazer o emprestimo com sucesso!')
else:
    print('\033[31mNEGADO!\033[m')
    print('Você não poderá tirar o emprestimo pois as mensalidades são superiores a 30% do seu salário.')
