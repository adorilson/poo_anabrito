# DESAFIO 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

quantidade = int(input("\nQuantos números deseja digitar? "))

numeros = []

for numero in range(quantidade):
    numero = int(input("Digite um número aqui: "))
    numeros.append(numero)

if numero in numeros:
    not numeros.append(numero)
    print("Número não adicionado!")

print(f"\nTodos os números ordenados na lista são esses → {sorted(numeros)}", end='\n\n')