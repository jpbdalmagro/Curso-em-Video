palavras = ('aprender', 'programar', 'estudar', 'linguagem', 'python', 'curso', 'gratis', 'praticar', 'trabalhar',
            'mercado', 'programador', 'futuro')


for palavra in palavras:
    print(f"As vogais na palavra {palavra.upper()} são ", end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(f"{letra} ", end='')
    print('\n', end='')
