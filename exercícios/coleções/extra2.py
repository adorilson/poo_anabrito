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



# DESAFIO 76 - LISTA DE PREÇO 
print()
lista = []
quantidade_produtos = int(input('Digite a quantidade de produtos: '))
for e in range(quantidade_produtos):
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    lista.append(produto)
    lista.append(valor)
print(f'\n LISTA DE PRODUTOS E PREÇOS \n {lista}', end='\n\n')



# DESAFIOS 74 E 78 - MAIOR E MENOR
# 1. Por que no desafio 78 foi usado um laço de repetição para inserir os dados, enquanto que no desafio 74 não foi usado?
# Seria possível usar laço de repetição no desafio 74. Se sim, faça essa mudança.

# RESPOSTA: Porque o desafio 74 solicita um programa que gere 5 números aleatórios, ou seja, o algoritmo que escolhe. 
# Enquanto o desafio 78 solicita que digitemos os valores que quisermos.
# Isso se trata de quem escolhe. Se é o programa (como no desafio 74) ou o programador (como no desafio 78).

# Acredito que não seria possível utilizar um laço de repetição com entrada de dados no desafio 74, 
# pois sua função é gerar números aleatórios.
# Entretanto, é possível utilizar um laço de repetição sem entrada de dados, 
# exatamente como está no programa do desafio 74.

# 2. Por que no desafio 74 foram usadas as funções max e min, enquanto que no desafio 78 foram usadas variáveis e
# estruturas condicionais? É possível usar max e min no desafio 78? É possível usar variáveis e estruturas
# condicionais no desafio 74? Se sim, faça essas mudanças.

# RESPOSTA: Porque as funções do desafio 74 permitem encontrar diretamente o maior e o menor valor de uma coleção, tornando o código mais simples.
# Enquanto no desafio 78 identifica o maior e o menor número digitado e suas respectivas posições na lista, utilizando variáveis e estruturas condicionais.
# Sim, é possível usar max e min no desafio 78.
# Sim, é possível usar variáveis e estruturas condicionais no desafio 74.



# DESAFIOS 79 - VALORES ÚNICOS
quantidade = int(input("\nQuantos números deseja digitar? "))
numeros = set()
for numero in range(quantidade):
    numero = int(input("Digite um número aqui: "))
    numeros.add(numero)

if numero in numeros:
    not numeros.add(numero)
    print("Número não adicionado!")
print(f"\nTodos os números ordenados na lista são esses → {sorted(numeros)}", end='\n\n')



# DESAFIOS 76 - TIMES DE FUTEBOL
produtos = {'arroz': 10,
            'feijão': 10,
            'carne': 50,
            'farofa': 20,
            'salada': 15,
            'suco': 5}

print()
for produto, preco in produtos.items():
    print(f'{produto} - R${preco}')
print()