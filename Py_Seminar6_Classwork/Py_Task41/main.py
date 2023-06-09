# Задача №41. Решение в группах.
# Дан массив, состоящий из целых чисел.
# Напишите программу, которая в данном массиве определит# количество элементов,
# у которых два соседних и, при этом, оба соседних элемента меньше данного.
# Сначала вводится число N — количество элементов в массиве.
# Далее записаны N чисел — элементы массива. Массив состоит из целых чисел.
#
# Ввод: 5
# Ввод: 1 2 3 4 5
# Вывод: 0
# Ввод: 5
# Ввод: 1 5 1 5 1
# Вывод: 2
# ------------------------------------------------------

lst = [1, 5, 1, 5, 1]
res = 0

for index in range(1, len(lst) - 1):
    if lst[index - 1] < lst[index] > lst[index + 1]:
        res += 1

print(f"-> Количество элементов, которые больше соседних слева и справа от них: {res}")
