from datetime import datetime as dt
sexo = int(input('''[1] - Masculino
[2] - Feminino
Digite seu sexo: '''))

while True:
    match sexo:
        case 1:
            ano_nasc = int(input('Digite o ano que você nasceu: '))
            ano = dt.today().year
            idade = ano - ano_nasc
            ano_alistamento = ano_nasc + 18

            if idade > 18:
                print(f'''Quem nasceu em {ano_nasc} faz {idade} em {ano}!
O ano do seu alistamento já passou!
Foi em {ano_alistamento}''')
            elif idade < 18:
                print(f'''Quem nasceu em {ano_nasc} faz {idade} em {ano}!
O ano do seu alistamento ainda não chegou!
será em {ano_alistamento}!''')
            else:
                print(f'''Quem nasceu em {ano_nasc} faz {idade} em {ano}!
            O seu alistamento é ESSE ANO!''')
            break
        case 2:
            print('Como seu sexo é feminino, voce não precisa se alistar!')
            decisao = str(input('Deseja proseguir? ')).strip()
            if decisao == 'sim':
                sexo = 1
            elif decisao == 'não':
                print('Certo, tenha um bom dia!')
                break
            else:
                print('Opção não suportada!')
                quit()
        case _:
            print('Opção não encontrada!')
            break
