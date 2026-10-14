# DESAFIO 91
# Crie um programa onde 4 jogadores lancem um dado e tenham resultados aleatórios.
# Guarde esses resultados em um dicionário. 
# No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

import random

print()

dicionario = {}

for jogador in range(4):
    id = int(input("Digite o número do jogador: "))
    dado = random.randint(1, 6)
    dicionario[id] = dado
    print(f'O jogador {id} recebeu o número {dado}', end='\n\n')

dicionario = dict(sorted(dicionario.items(), key=lambda item: item[1], reverse=True))

print(f'Os jogadores vencedores são {dicionario}', end='\n\n')