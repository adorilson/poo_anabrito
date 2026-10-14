# DESAFIO 76
# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

print()

produtos = ('arroz', 10,
            'feijão', 10,
            'carne', 50,
            'farofa', 20,
            'salada', 15,
            'suco', 5)

for pos in range(0, len(produtos)):
    if pos % 2:
        print(f"R${produtos[pos]}")
    else:
        print(produtos[pos], end=" - ")
print()