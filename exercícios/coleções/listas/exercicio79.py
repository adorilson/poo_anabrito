# DESAFIO 79
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

quantidade = int(input("Quantos números deseja digitar? "))

numeros = []

for numero in range(quantidade):
    numeros.append(int(input("Digite um número aqui: ")))

if numero in numeros:
    not numeros.append(numero)
    print("Número não adicionado!")

print()
print(f"\nTodos os números ordenados na lista são esses → {sorted(numeros)}", end='\n\n')