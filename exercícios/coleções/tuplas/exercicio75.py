# DESAFIO 75
# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em tuplas. 
# No final, mostre: A) Quantas vezes apareceu q; B) Em que posição foi digitado o primeiro valor 3; C) Quais foram os números pares.

print()

numeros = []

for valor in range(4):
    numeros.append(int(input("Digite um número aqui: ")))

tupla = tuple(numeros)

print(f"\nVocê digitou os números → {tupla}")
print(f"O número 13 apareceu {numeros.count(13)}x na tupla.")

pos_num3 = numeros.index(3)
if 3 in numeros:
    print(f"O número 3 foi digitado na posição {pos_num3 + 1}.")
else:
    print(f"A tupla não possui o número 3.")

pares = []
for indice, numero in enumerate(numeros):
    if numero % 2 == 0:
        pares.append(numero)
print(f"A lista dos números pares → {pares}", end='\n\n')