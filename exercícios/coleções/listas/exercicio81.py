# DESAFIO 81
# Crie um programa que vai ler vários números e colocar numa lista.
# Depois disso, mostre: A)Quantos números foram digitados; B)A lista de valores, ordenada da forma descrescente; C)Se o valor 5 foi digitado e está ou não na lista; 

print()

quantidade = int(input("Quantos números deseja digitar? "))

numeros = []

for numero in range(quantidade):
    numeros.append(int(input("Digite um número aqui: ")))

numeros.sort(reverse=True)

print(f"\nOs números na lista ordenada são esses → {sorted(numeros)}")
print(f"Foram digitados {len(numeros)} números.")
print(f"Os números em ordem descrescente são esses → {numeros}")
if 5 in numeros:
    print(f"O número 5 apareceu na lista.", end='\n\n')
else:
    print(f"O número 5 não apareceu na lista.", end='\n\n')