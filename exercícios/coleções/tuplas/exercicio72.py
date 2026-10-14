# DESAFIO 72
# Crie um programa que tenha uma tipla totalmente preenchida com uma contagem por extenso, de zero até vinte.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

print()

num_extenso = ('zero', 'um', 'dois', 'três','quatro', 'cinco', 'seis', 
'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze','catorze', 
'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

ler_numero = int(input("Digite um número entre 0 e 20: "))

print(f"\n{num_extenso[ler_numero]}", end='\n\n')