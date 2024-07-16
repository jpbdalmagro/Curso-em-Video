salario = float(input('Digite o seu salário: R$'))

if salario > 1250:
    salario = salario + salario * 0.10
    aumento = 10
else:
    salario = salario + salario * 0.15
    aumento = 15

print('Você receberá um aumento de {}% e passará a receber R${:.2f}.'.format(aumento, salario))
