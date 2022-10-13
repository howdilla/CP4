from random import random

# Зададим максимально возможное число (a), которое может оказаться в дальнейшем массиве.
a = int(input('Введите максимально возможное число, которое может встретиться в массиве:'))

# Зададим количество чисел в массиве (N).
N = int(input('Задайте количество чисел в массиве:'))

# Создаём массив с нулями, а затем заполняем его рандомными числами.
array = [0] * N

for i in range(N):
    array[i] = random() * a

print(array)

# Найдём максимальный элемент в массиве.
max_number = max(array)

print(max_number)

# Найдём место, на котором стоит максимальный элемент
number = 0

for j in range(N):
    if array[j] == max_number:
        number = j + 1

print(number)

# Элементы, стоящие после максимального, заменяем нулями

for l in range(number, N):
    array[l] = 0

print(array)
