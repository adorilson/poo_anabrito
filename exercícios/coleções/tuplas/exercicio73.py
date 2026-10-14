# DESAFIO 73
# Crie uma tupla preenchida com os 20 primerios colocados da tabel a do Campeonato Brasileiro de Futebol, na ordem de colocação.
# Depois mostre: A) Apenas os 5 primeiros colocados; B) Os últimos 4 colocados; C) Uma lista com os times em ordem alfabética; D) Em que posição está o time Chapeconense;

times_campeonatobr = ('Flamengo', 'Palmeiras', 'Athletico-PR', 'Fluminense', 'Bahia', 
'Cruzeiro', 'Coritiba', 'Atlético-MG', 'Red Bull Bragantino', 'Corinthians', 'São Paulo', 
'Botafogo', 'Vitória', 'Santos', 'Grêmio', 'Mirassol', 'Vasco', 'Internacional', 'Remo', 'Chapecoense')

print()
print(f"Os 5 primeiros colocodos do Brasileirão: {times_campeonatobr[0:6]}", end='\n\n')
print(f"Os 4 últimos colocados do Brasileirão: {times_campeonatobr[-4:]}", end='\n\n')
print(f"Os times do Brasileirão em ordem alfabética: {sorted(times_campeonatobr)}", end='\n\n')

pos_chape = times_campeonatobr.index('Chapecoense') + 1
print(f"O time Chapecoense está na posição: {pos_chape}", end='\n\n')

print(f"Quantidade de times: {len(times_campeonatobr)}", end='\n\n')

for pos, time in enumerate(times_campeonatobr):
    print(pos + 1, end='')
    print(' - ', end='') 
    print(time)
print()