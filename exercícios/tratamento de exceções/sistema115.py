from funcoes115 import menu, leia_opcao, lista_pessoas, cadastra_pessoa

menu()

opcao = leia_opcao()

if opcao == 1:
    print('Opcao 1 selecionada')
    print('Listagem de pessoas')
    lista_pessoas()
elif opcao == 2:
    print('Opcao 2 selecionada')
    print('Cadastro de uma nova pessoa')
    cadastra_pessoa()
    
    lista_pessoas()
elif opcao == 3:
    print('Obrigado por usar o sistema.')
else:
    print('Opcao de menu inválida.')