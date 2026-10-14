# DESAFIO 80
# Crie um programa onde o usuário possa digitar cinco valores numéricos.
# Cadastre-os em uma lista, já na posição correta de inserção (sem usar o "sort()").
# No final, mostre a lista ordenada na tela.

print()

numeros = []

for numero in range(5):
    numeros.append(int(input("Digite um número aqui: ")))

print(f"\nTodos os números ordenados na lista são esses → {sorted(numeros)}", end='\n\n')