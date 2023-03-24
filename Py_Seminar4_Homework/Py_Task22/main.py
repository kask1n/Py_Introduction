# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12
# ------------------------------------------------------

# from random import randint
#
# a = int(input("Введите количество чисел для 1-го набора: "))
# b = int(input("Введите количество чисел для 2-го набора: "))
# list_a = [randint(1, 19) for i in range(a)]
# list_b = [randint(1, 19) for i in range(b)]
# print(f"{list_a}\n{list_b}")
#
# # for i in range(a):
# #     list_a.append(randint(1, 10))
# # for i in range(b):
# #     list_b.insert(i, randint(1, 10))
#
# list_a = set(list_a)
# list_b = set(list_b)
# print(f"{list_a}\n{list_b}")
#
# result = list_a.intersection(list_b)
# print(result)
#
# result = list(list_a.intersection(list_b))
# print(result)
#
# result.sort()
# print(result)

# for i in range(len(list_i)-1):
#     for j in range(i+1, len(list_i)):
#         if list_i[j] < list_i[i]:
#             temp = list_i[i]
#             list_i[i] = list_i[j]
#             list_i[j] = temp
# print(*list_i)
#
# for i in range(len(list_i) - 1):
#     for j in range(i + 1, len(list_i)):
#         if list_i[j] < list_i[i]:
#             list_i.insert(i, list_i.pop(j))
#
# print('Общие элементы по возрастанию:', *list_i)


mol = [x for x in input().split()]
n = mol[0]
m = mol[1]
set_1 = set()
set_2 = set()
list_1 = list()
a = [x for x in input().split()]
k = set(a)
for i in k:
    set_1.add(i)
b = [x for x in input().split()]
k1 = set(b)
for i in k1:
    set_2.add(i)
lok = set_1 & set_2
kool = list(lok)
kool.sort()
for i in kool:
    print(i, end=' ')
