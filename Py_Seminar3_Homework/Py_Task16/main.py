# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1...N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
#
# Input N: 5
# Output: 1 2 3 4 5
# Input X: 3
# Output: -> 1
# ------------------------------------------------------

from random import randint

flag = True
while flag:
    n = int(input("Введите количество элементов (N≥1): "))
    if n > 0:
        flag = False
    else:
        print("Введено некорректное значение!")

list_a = [randint(1, 9) for i in range(n)]
print("->", *list_a)

flag = True
while flag:
    x = int(input("Введите искомое число (X≥1): "))
    if x > 0:
        flag = False
    else:
        print("Введено некорректное значение!")

count = 0
for i in list_a:
    if x == i:
        count += 1

print(f"Количество элементов со значением {x}: {count}")
