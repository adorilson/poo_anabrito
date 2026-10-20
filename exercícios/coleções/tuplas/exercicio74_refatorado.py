# EXERCÍCIO EXTRA 2 - MANIPULAÇÃO DE COLEÇÕES

# DESAFIOS 74 E 78 - MAIOR E MENOR

import random

tupla = []

for numero in range(5):
    numeros_aleatorios = random.randint(1, 10)
    tupla.append(numeros_aleatorios)

maior = tupla[0]
menor = tupla[0]

for numero in tupla:
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero

tupla_ordenada = tuple(sorted(tupla))

print(f"\nOs números gerados aleatoriamente em ordem crescente são: {tupla_ordenada}")
print(f"O menor número é: {menor}")
print(f"O maior número é: {maior}", end='\n\n')