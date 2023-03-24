# def sum_numbers(n, y='Hello'):  # Если не передаём y, то берётся значение по умолчанию.
#     print(y)
#     sum = 0
#     for i in range(1, n + 1):
#         sum += i
#     return sum
#     # print('stop')  # Не выполняется, т.к. находится после return.
#
#
# a = sum_numbers(5, 'qwert')
# print(a)

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += str(i)
#     return res
#
#
# print(sum_str('q', 'e', 'l'))
# print(sum_str('q', 'e', 'l', 'r', 'f'))
# print(sum_str(1, 8, 9))

# from modul1 import max1  # Импортировать из модуля требуемую функцию.
# from modul1 import *  # Импортировать из модуля все функции.
# import modul1 as m1  # Импортировать модуль целиком и присвоить ему удобную метку (m1).
#
# print(m1.max1(10, 9))

# def fib(n):
#     # print(n)  # При отсутствии базиса рекурсии (if) функция будет выполняться бесконечно.
#     if n in [1, 2]:
#         return 1
#     return fib(n - 1) + fib(n - 2)
#
#
# list_1 = []
# for i in range(1, 10):  # [1, 9] - первые 9 элементов последовательности Фибоначчи.
#     list_1.append(fib(i))
# print(list_1)

# БЫСТРАЯ СОРТИРОВКА:
# def quick_sort(array):
#     if len(array) <= 1:  # Базис рекурсии.
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot]
#     return quick_sort(less) + [pivot] + quick_sort(greater)  # Можем складывать списки только со списками.
#
#
# print(quick_sort([14, 5, 9, 6, 3, 58, 7, 5, 2, 7]))
# print(quick_sort([10, 5, 2]))  # [2, 5, 10]


# СОРТИРОВКА СЛИЯНИЕМ:
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1


list1 = [1, 5, 6, 9, 8, 7, 2, 1, 55, 2, 4]
merge_sort(list1)
print(list1)
