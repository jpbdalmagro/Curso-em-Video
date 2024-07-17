tabela = ('Botafogo', 'Palmeiras', 'Flamengo', 'Bahia', 'Cruzeiro', 'São Paulo', 'Fortaleza', 'Athletico-PR',
          'Bragantino', 'Atlético-MG', 'Vasco', 'Inter', 'Juventude', 'Criciúma', 'Cuiabá', 'Vitória', 'Corinthians',
          'Grêmio', 'Atlético-GO', 'Fluminense')
print("-" * 30)
print(f"Lista de times do brasileirão: {tabela}")
print("-" * 30)
print(f"Os cinco primeiros colocados são {tabela[:5]}")
print("-" * 30)
print(f"Os quatro ultimos são {tabela[16:]}")
print("-" * 30)
print(f"Os times em ordem alfabética são: {sorted(tabela)}")
print("-" * 30)
print(f"O Grêmio está na {tabela.index('Grêmio') + 1}ª posição.")
