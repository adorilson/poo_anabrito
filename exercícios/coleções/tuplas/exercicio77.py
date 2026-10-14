# DESAFIO 77
# Crie uma programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

palavras =('ana', 'volei',
           'xadrez', 'patinacao',
           'academia', 'luta',
           'praia', 'festa',
           'spotify', 'livros',
           'cinema', 'instrumentos',
           'cubos', 'sudoku'
           'natacao', 'marinha',
           'azul', 'bege',
           'gremio', 'amizade',
           'poesia', 'amor',
           'culinaria', 'idiomas',
           'lugares', 'monumentos',
           'programacao', 'instituto')

for palavra in palavras:
    print(f"\nA palavra {palavra.upper()} possiu as vogais ", end='')
    for letra in palavra:
        if letra in 'aeiou':
            print(letra, end=' ')
print('\n')