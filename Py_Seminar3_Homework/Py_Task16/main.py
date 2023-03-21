# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N].
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X.
# Input N: 5
# Output: 1 2 3 4 5
# Input X: 3
# Output: -> 1
# ------------------------------------------------------

from random import randint

n = int(input("Введите количество элементов (N): "))
a = []
for i in range(n):
    a.insert(i, randint(0, 9))
print(*a)

x = int(input("Введите искомое число (X): "))
count = 0
for i in a:
    if x == i:
        count += 1
print(f"Количество элементов со значением {x} = {count}")


# from random import randint
# a = []
# n = int(input("Введите количество числе в списке:  "))
# x = int(input("Искомое число:  "))
# for i in range(n):
#     a.append(randint(1,10))
# i = 0
# count = 0
# while i < n:
#     if a[i]==x:
#         count+=1
#     i+=1
# print(a)
# print(count)