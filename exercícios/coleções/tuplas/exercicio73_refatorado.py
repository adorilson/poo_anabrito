# EXERCICIO EXTRA 2 - MANIPULACAO DE COLEÇÕES

# DESAFIO 73 - TIMES DE FUTEBOL

times_campeonatobr = []

quantidade_times = int(input('\nDigite a quantidade de times classificados: '))

for e in range(quantidade_times):
    times = str(input('Digite os times classificados: '))
    times_campeonatobr.append(times)

print('\nCLASSIFICAÇÃO DO CAMPEONATO')

for pos, times in enumerate(times_campeonatobr):
    print(f'{pos + 1} - {times}')



classificacao_especifica = []

quantidade_time_especifico = int(input('\nDe quantos times deseja ver a classificação? '))

for e in range(quantidade_time_especifico):
    time_desejado = str(input('De qual time deseja ver a classificação? '))
    classificacao_especifica.append(time_desejado)

print(f'\nCLASSIFICAÇÃO ESPECÍFICA')

for time_desejado in classificacao_especifica:
    if times in times_campeonatobr:
        pos = times_campeonatobr.index(time_desejado)
        print(f'{pos + 1} - {time_desejado}')
    else:
        print('Time não encontrado!')
print()