from exercicio104 import leiaInt

pessoas = [('Ana', 18),
           ('Giovana', 15),
           ('EU', 42), 
          ]

def menu():
    print('-'*15)
    print('MENU PRINCIPAL')
    print('-'*15)
    print('1 - Ver pessoas cadastradas')
    print('2 - Cadastrar pessoas')
    print('3 - Sair')


def leia_opcao():
    opcao = leiaInt('Sua opção: ')

    return opcao

def lista_pessoas():
    for pessoa in pessoas:
        print(f'Nome={pessoa[0]} - Idade={pessoa[1]}')

def cadastra_pessoa():
    nome = input('Digite o nome:')
    idade = leiaInt('Digite a idade:')
    pessoa = nome, idade
    pessoas.append(pessoa)