# EXERCICIO EXTRA 2 - MANIPULACAO DE COLEÇÕES

# DESAFIO 76 - LISTA DE PREÇO 

lista = []

quantidade_produtos = int(input('\nDigite a quantidade de produtos: '))

for e in range(quantidade_produtos):
    produto = str(input('Digite o nome do produto: '))
    valor = float(input('Digite o valor do produto: '))
    lista.append(produto)
    lista.append(valor)

print(f'\nLISTA DE PRODUTOS E PREÇOS \n {lista}', end='\n\n')