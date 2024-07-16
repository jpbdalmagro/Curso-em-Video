while True:
    lado_a = float(input('Digite o lado a do triângulo: '))
    lado_b = float(input('Digite o lado b do triãngulo: '))
    lado_c = float(input('Digite o lado c do triângulo: '))

    if lado_a + lado_b > lado_c and lado_a + lado_c > lado_b and lado_c + lado_b > lado_a:
        if lado_a == lado_b and lado_a == lado_c:
            print('Você terá um triângulo equilátero.')
        elif lado_a == lado_b or lado_c == lado_b or lado_a == lado_c:
            print('Você terá um triângulo isóceles.')
        else:
            print('Você terá um triângulo escaleno.')
    else:
        print('Você não pode formar um triângulo.')

    if input('Dnv? ') == 'n':
        break
