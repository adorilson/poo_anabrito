# EXERCÍCIO EXTRA 2 - MANIPULAÇÃO DE COLEÇÕES

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