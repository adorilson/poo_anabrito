# DESAFIO 104
# Crie um programa que tenha a função leiaInt(), que vai funcionar semelhante à função input() do Python, 
# só que fazendo a validação para aceitar apenas um número numérico.
# A função deverá solicitar um número, se o que usuário digitar for realmente um número, a função deve retornar esse valor. 
# Caso contrário, ela deve solicitar novamente, até que usuário digite um número.

def leiaInt(mensagem):
    while True:
        n = input(mensagem)
        if n.isdigit():
            print(f'Você acabou de digitar o número {n}')
            return int(n)
        else:
            print('ERRO! Digite um número válido')


if __name__ == '__main__':
    numero = leiaInt('\nDigite um número: ')
    print(f'{numero=}')