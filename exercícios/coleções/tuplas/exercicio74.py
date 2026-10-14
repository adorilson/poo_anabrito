# DESAFIO 74
# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

import random

tupla = []

for numero in range(5):
    numeros_aleatorios = random.randint(1, 10)
    tupla.append(numeros_aleatorios)

tupla_ordenada = tuple(sorted(tupla))

print()
print(f"Números gerados aleatoriamente em ordem crescente: {tupla_ordenada}")
print(f"O menor número é: {min(tupla_ordenada)}")
print(f"O maior número é: {max(tupla_ordenada)}", end='\n\n')