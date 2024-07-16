print('{:-^40}'.format(' LOJAS DAL MAGRO '))
preco = float(input('Digite o valor total das compras: R$'))
print('''\n FORMAS DE PAGAMENTO
[1] - A VISTA (DINHEIRO / CHEQUE)
[2] - A VISTA (CARTÃO)
[3] - 2x NO CARTÃO
[4] - 3x OU MAIS NO CARTÃO''')

pagamento = int(input('Digite a forma de pagamento: '))

match pagamento:
    case 1:
        preco -= preco * 10 / 100
        print('Com essa forma de pagamento você ganha 10% de desconto e precisará pagar apenas R${:.2f}.'.format(preco))
    case 2:
        preco -= preco * 5 / 100
        print('Com essa forma de pagamento você ganha 5% de desconto e precisará pagar apenas R${:.2f}.'.format(preco))
    case 3:
        print('Com essa forma de pagamento você pagará o valor integral de R${} em 2 parcelas de R${:.2f}.'.format(
            preco, preco / 2))
    case 4:
        preco += preco * 20 / 100
        print('Com essa forma de pagamento o valor aumenta em 20% totalizando R${:.2f}.'.format(preco))
        parcelas = int(input('Digite em quantas vezes você deseja parcelar: '))
        if parcelas == 1:
            print('Para pagamentos a vista selecione a opção 2.')
        elif parcelas == 2:
            print('Para pagamentos em até duas parcelas selecione a opção 3.')
        else:
            print('Com {} parcelas você pagará R${:.2f} mensalmente.'.format(parcelas, preco / parcelas))
    case _:
        print('Forma de pagamento não encontrada!')
