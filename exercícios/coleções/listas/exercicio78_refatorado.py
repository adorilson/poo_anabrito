# EXERCÍCIO EXTRA 2 - MANIPULAÇÃO DE COLEÇÕES

# DESAFIOS 74 E 78 - MAIOR E MENOR

numeros = []

print()
for numero in range(5):
    numeros.append(int(input("Digite um número aqui: ")))

maior = max(numeros)
menor = min(numeros)

pos_max = numeros.index(maior)
pos_min = numeros.index(menor)

print(f"\nO maior valor digitado foi {maior} na posição {pos_max + 1}.")
print(f"O menor valor digitado foi {menor} na posição {pos_min + 1}.", end='\n\n')