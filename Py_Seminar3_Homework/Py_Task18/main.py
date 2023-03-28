# Задача 18: В массиве A[1...N] требуется найти самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка выводит самый близкий элемент к X.
#
# Input N: 5
# Output: 1 2 3 4 5
# Input X: 6
# Output: -> 5
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
    x = input("Введите искомое вещественное число (X): ")
    try:
        x = float(x)
        flag = False
    except ValueError:
        print('-> ОШИБКА: Введено некорректное значение!')


# result = 0
# difference = 0
# flag = True
# while not result:  # Возвращает ПОСЛЕДНЕЕ вхождение (если порядок не важен, то лишние итерации).
#     for item in list_a:  # Работает только с целыми числами.
#         if abs(x - item) == difference:
#             result = item
#             flag = False
#
#     difference += 1

def nearest_number_int(list, find):  # Возвращает ПЕРВОЕ вхождение (предпочтительнее, если порядок не важен).
    difference = 0  # Работает только с целыми числами.
    while True:
        for item in list:
            if abs(find - item) == difference:
                return item
        difference += 1


# print(f"Самый близкий по величине элемент к заданному числу ({x}): {nearest_number_int(list_a, x)}")


def nearest_number_float(list, find):  # Сразу возвращает ИСКОМОЕ, ИНАЧЕ БЛИЖАЙШЕЕ к искомому (полный цикл).
    diffs = set()  # Работает со всеми вещественными числами.
    for item in list:
        diff = abs(find - item)

        if not diff:
            return item
        else:
            diffs.add(diff)

    if find - min(diffs) in list:  # Если искомое равноудалено от двух - выведет меньшее по значению.
        return find - min(diffs)
    else:
        return find + min(diffs)

    # for index in range(len(list)):  # Работает по индексу без дополнительного списка.
    #     diff = abs(find - list[index])
    #     if not diff:
    #         return list[index]
    #     else:
    # elif min_diff < abs(find - list[index]):
    # min_diff = abs(find - list[index])


print(f"Самый близкий по величине элемент к заданному числу ({x}): {round(nearest_number_float(list_a, x))}")

# from random import randint as RD
# n = int(input("Введите количество элементов массива : "))
# a = [RD(0,100) for _ in range(n)]
# print("Массив состоит из: ", *a)
# x = int(input("Введите элемент массива : "))
# a.sort()
# print("Отсортированный массив: ", *a)
# a.append(x)
# a.sort()
# q = list_a.index(x)
# if q!= len(a) and q!=0 and a[q-1]- x <= a[q+1]-x : print("Ближайший элемент:", a[q-1])
# else: print(f"К числу  {x} ближайший элемент:", a[q+1])


# from random import randint
# a = []
# n = int(input("Введите количество числе в списке:  "))
# x = int(input("Искомое число:  "))
# for i in range(n):
#     a.append(randint(1,10))
# print(a)
# j = 0
# find_res = 0
# flag = True
# while find_res == 0:
#     i = 0
#     while i<n and flag:
#         if abs(x-a[i])==j:
#             find_res = a[i]
#             flag = False
#         i+=1
#     j+=1
