# DESAFIO 83
# Crie um programa onde o usuário digite um expressão qualquer que use parênteses.
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

print()

expressao = str(input("Digite uma expressão aqui: "))

pilha = []

for simbolo in expressao:
    if simbolo == "(":
        pilha.append("(")
    elif simbolo == ")":
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(")")

if len(pilha) == 0:
    print("\nSua expressão é válida!", end="\n\n")
else:
    print("\nSua expressão não é válida!", end="\n\n")