# DESAFIO 82
# Crie um programa que vai lar vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão contar apenas os valores pares e ímpares digitados, respectivamente.
# No final, mostre o conteúdo das três listas geradas.

print()

quantidade = int(input("Quantos números deseja digitar? "))

numeros = []

for numero in range(quantidade):
    numeros.append(int(input("Digite um número aqui: ")))

pares = []
impares = []

for indice, numero in enumerate(numeros):
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print(f"\nA lista com todos os números → {numeros}")
print(f"A lista dos números pares → {pares}")
print(f"A lista dos números impares → {impares}", end='\n\n')