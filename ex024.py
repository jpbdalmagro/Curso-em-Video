cidade = str(input('Digite o nome de uma cidade: ')).strip()
verifica_santo = cidade.lower()[:5] == "santo"
if verifica_santo:
    print('Sua começa com "Santo".')
else:
    print('Sua cidade não começa com "Santo".')
