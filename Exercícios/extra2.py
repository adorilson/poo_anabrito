# EXERCICIO EXTRA - MANIPULACAO DE COLECOES

a = [0, 1, 2, 3, 4, 5, 5, 0]
b = [4, 5, 6, 7, 8, 9, 9, 4]

# 1. Ler os valores das coleções a e b;
print(a, b)

# 2. Exibir os valores distintos, sem repetições, de cada coleção;
def remove_repeticao_a(a):
    return set(a)
r1 = remove_repeticao_a(a)
print(r1)

def remove_repeticao_a(b):
    return set(b)
r2 = remove_repeticao_a(b)
print(r2)

# 3. Exibir os valores presentes em a, mas que não estão presentes em b (diferença a - b);
def remove_diferenca_a(a, b):
    return set(a - b)
d1 = remove_diferenca_a(a, b)
print(d1)

# 4. Exibir os valores presentes em b, mas que não estão presentes em a (diferença b - a);
def remove_diferenca_b(a, b):
    return set(b - a)
d2 = remove_diferenca_a(a, b)
print(d2)

# 5. Exibir os valores presentes em a ou em b, considerando cada valor apenas uma vez (união de a e b);