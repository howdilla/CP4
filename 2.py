# Введём размерность массива А.
N = int(input('Введите размерность массива А:'))

# Cоздадим массив А с нулями.
A = [0] * N

# Введём N-элементов массива А.
for i in range(N):
    A[i] = int(input('Введите элемент массива A:'))

print(A)

# Введём размерность массива B.
M = int(input('Введите размерность массива B:'))

# Cоздадим массив B с нулями.
B = [0] * M

# Введём M-элементов массива B.
for j in range(N):
    B[j] = int(input('Введите элемент массива B:'))

print(B)

# Создадим пустой массив S, куда будем добавлять общие для А и В элементы.
S = []

# Проходим по двум массивам и ищем общие элементы.
for l in A:
    for k in B:
        if l == k:
            S.append(l)

print(S)


