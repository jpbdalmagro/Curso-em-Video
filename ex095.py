"""Aprimore o exercicio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
do aproveitamento de cada jogador."""


def cadastrar(d: dict, dados=None) -> dict:
    if dados is None:
        dados = {}
    print('-' * 45)
    print("CADASTRO DE JOGADOR")
    nome = str(input("Digite o nome do jogador: ")).strip().capitalize()
    dados['jogos'] = int(input(f"Digite o número de jogos de {nome}: "))
    dados['gols'] = [int(input(f"Quantos gols {nome} fez no {i + 1}º jogo: ")) for i in range(dados['jogos'])]
    dados['total_gols'] = sum(dados['gols'])
    dados['media_gols'] = round(dados['total_gols'] / dados['jogos'], 2)
    dados['aproveitamento'] = str(round(
        (len(dados['gols']) - dados['gols'].count(0)) * 100 / len(dados['gols']), 2)) + '%'

    d[nome] = dados.copy()

    print(f"\033[1;32mJogador {nome} cadastrado com sucesso.\033[m")

    return d.copy()


def ranking(d: dict):
    if d:
        top_gols = {'nome': '', 'gols': 0}
        top_partidas = {'nome': '', 'jogos': 0}
        top_media = {'nome': '', 'media_gols': 0}
        top_aproveitamento = {'nome': '', 'aproveitamento': '0%'}

        for jogador, dados in d.items():
            if dados['total_gols'] > top_gols['gols']:
                top_gols['nome'] = jogador
                top_gols['gols'] = dados['total_gols']

            if dados['jogos'] > top_partidas['jogos']:
                top_partidas['nome'] = jogador
                top_partidas['jogos'] = dados['jogos']

            if dados['media_gols'] > top_media['media_gols']:
                top_media['nome'] = jogador
                top_media['media_gols'] = dados['media_gols']

            if float(dados['aproveitamento'].strip('%')) > float(top_aproveitamento['aproveitamento'].strip('%')):
                top_aproveitamento['nome'] = jogador
                top_aproveitamento['aproveitamento'] = dados['aproveitamento']

        print('-' * 45)
        print(f'{"Ranking de Jogadores":^45}')
        print('-' * 45)
        print(f"GOLS: {top_gols['nome']} - {top_gols['gols']} gols")
        print(f"PARTIDAS: {top_partidas['nome']} - {top_partidas['jogos']} jogos")
        print(f"MEDIA: {top_media['nome']} - {top_media['media_gols']} gols por partida")
        print(
            f"APROVEITAMENTO: {top_aproveitamento['nome']} - {top_aproveitamento['aproveitamento']} partidas com gols")

        input('Pressione Enter para continuar')

    else:
        print("Nenhum jogador cadastrado até o momento.")


def dados_jogadores(d: dict):
    if d:
        while True:
            nomes = [nome for nome in d.keys()]
            print()
            print(nomes)
            while True:
                escolha = input('Digite o nome do Jogador que gostaria de avaliar: ').strip().capitalize()

                if escolha in nomes:
                    break
                else:
                    print(f"Jogador {escolha} não consta no banco de dados!")

            escolhido = d[escolha]

            print('-' * 45)
            print(f'{"Dados de " + escolha:^45}')

            for dado, valor in escolhido.items():
                if dado != 'gols':
                    print(f"{dado:<23}{valor:>22}")
            print('-' * 45)
            print(f"{'Resumo dos jogos:':^45}")

            for i, gol in enumerate(escolhido['gols']):
                print(f"Na rodada {i} {escolha} fez {gol} gol(s)")

            if input("Deseja ver outro: ").lower()[0] == 'n':
                break

    else:
        print("Nenhum jogador cadastrado até o momento.")


def excluir_players(d: dict):
    if d:
        while True:
            nomes = [nome for nome in d.keys()]
            print()
            print(nomes)
            while True:
                escolha = input('Digite o nome do Jogador que gostaria de excluir: ').strip().capitalize()

                if escolha in nomes:
                    break
                else:
                    print(f"Jogador {escolha} não consta no banco de dados!")

            del d[escolha]
            print(f"\033[1;32mJogador {escolha} deletado com sucesso.\033[m")

            if input("Deseja ver outro: ").lower()[0] == 'n':
                break

    else:
        print("Nenhum jogador cadastrado até o momento.")

    return d.copy()


def main(players):
    print("-=-" * 15)
    print(f"{'CENTRAL DE ESTATISTICAS DE JOGADORES':^45}")
    print("-=-" * 15)
    print(f"{'1 - Cadastrar novo jogador':^45}")
    print(f"{'2 - Ver ranking de jogadores':^45}")
    print(f"{'3 - Ver informações de cada jogador':^45}")
    print(f"{'4 - Deletar jogador':^45}")
    print(f"{'5 - Sair':^45}")
    print("-=-" * 15)

    escolha = str(input("Digite a opção desejada: ")).strip()

    match escolha:
        case '1':
            players = cadastrar(players)

        case '2':
            ranking(players)

        case '3':
            dados_jogadores(players)

        case '4':
            players = excluir_players(players)

        case '5':
            return

        case _:
            print("\033[1;31m Opção inválida!\033[m")

    return main(players)


if __name__ == '__main__':
    jogadores = {}
    main(jogadores)
