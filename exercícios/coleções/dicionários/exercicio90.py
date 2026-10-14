# DESAFIO 90
# Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário.
# No final, mostre mostre o conteúdo da estrutura na tela.

print()

dados = {}
info = []

for d in range(1):
    dados['nome'] = str(input("Digite o nome do aluno: "))
    dados['media'] = int(input("Digite a média do aluno: "))
    info.append(dados)
    print(end='\n')

print(info, end='\n\n')