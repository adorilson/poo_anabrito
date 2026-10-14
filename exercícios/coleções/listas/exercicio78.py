# DESAFIO 78
# Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menos valor digitado e suas respectivas posições na lista.

print()

numeros = []

for numero in range(5):
    numeros.append(int(input("Digite um número aqui: ")))

pos_max = numeros.index(max(numeros))
pos_min = numeros.index(min(numeros))

print(f"\nO maior valor digitado foi {max(numeros)} na posição {pos_max + 1}.")
print(f"O menor valor digitado foi {min(numeros)} na posição {pos_min}.", end='\n\n')