<<<<<<< HEAD
# EXERCICIO EXTRA 1 - MANIPULACAO DE COLEÇÕES

a = [0, 1, 2, 3, 4, 5, 5, 0]
b = [4, 5, 6, 7, 8, 9, 9, 4]

print()

# 1 - Ler os valores das coleções a e b;
print(f'1 - Os valores de A são {a} e B são {b}', end='\n\n')

# 2 - Exibir os valores distintos, sem repetições, de cada coleção;
def remove_repeticao_a(a):
    return set(a)
r1 = remove_repeticao_a(a)
def remove_repeticao_a(b):
    return set(b)
r2 = remove_repeticao_a(b)
print(f'2 - Os valores distintos de A são {r1} e B são {r2}', end='\n\n')

# 3 - Exibir os valores presentes em a, mas que não estão presentes em b (diferença a - b);
def remove_diferenca_a(a, b):
    rd = set(a) 
    rd.difference_update(b) 
    return rd
d1 = remove_diferenca_a(a, b)
print(f'3 - Os valores que estão em A, mas não estão em B são {d1}', end='\n\n')

# 4 - Exibir os valores presentes em b, mas que não estão presentes em a (diferença b - a);
def remove_diferenca_b(a, b):
    rd = set(b) 
    rd.difference_update(a) 
    return rd
d2 = remove_diferenca_a(a, b)
print(f'4 - Os valores que estão em B, mas não estão em A são {d2}', end='\n\n')

# 5 - Exibir os valores presentes em a ou em b, considerando cada valor apenas uma vez (união de a e b);
def uniao(a, b):
    u = set(a) 
    u.update(b) 
    return u
u = uniao(a, b)
print(f'5 - Os valores sem repetição que estão em A e B são {u}', end='\n\n')

# 6 - Exibir os valores presentes, simultaneamente, em a e b (interseção de a e b);
def intersecao(a, b):
    i = set(a)
    i.intersection_update(b)
    return i
i = intersecao(a, b)
print(f'6 - Os valores simultâneos que estão em A e B são {i}', end='\n\n')


# 7 - Exibir os valores presentes em exatamente uma das duas coleções, ou seja, em a ou b, mas não em ambas (diferença simétrica de a e b).
def diferenca_simetrica(a, b):
    ds = set(a)
    ds.intersection_update(b)
    return ds
ds = diferenca_simetrica(a, b)
print(f'7 - Os valores da diferença simétrica que estão em A e B são {ds}', end='\n\n')
=======
# EXERCICIO EXTRA - MANIPULACAO DE COLECOES




def remove_repeticao(lista):
    c = []
    for elemento in lista:
        if elemento not in c:
            c.append(elemento)

    return c



# principal
a = [0, 1, 2, 3, 4, 5, 5, 0]
b = [4, 5, 6, 7, 8, 9, 9, 4]


print(a, b)

a_sem_repeticao = remove_repeticao(a)
b_sem_repeticao = remove_repeticao(b)

print(a_sem_repeticao, b_sem_repeticao)
>>>>>>> f267ecff0ae2b7e5a9fea1f693fb79f38c9ad6cf
