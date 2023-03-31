# Задача №25. Решение в группах.
# Напишите программу, которая принимает на вход строку и отслеживает,
# сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# ------------------------------------------------------

# РЕШЕНИЕ 1 ЧЕРЕЗ PRINT БЕЗ ДОПОЛНИТЕЛЬНЫХ СПИСКОВ:

lst = input("Введите символы через пробел: ").split()
print(*lst)
dictionary = {}

for char in lst:
    if char not in dictionary.keys():
        dictionary.update({char: 0})
        print(f"{char} ", end="")
    else:
        dictionary[char] += 1
        print(f"{char}_{dictionary[char]} ", end="")
# ------------------------------------------------------

# РЕШЕНИЕ 2 ЧЕРЕЗ ДОПОЛНИТЕЛЬНЫЙ СПИСОК:

# lst = input("Введите символы через пробел: ").split()
# dictionary = {}
# result_lst = []
# for item in lst:
#     if item not in dictionary.keys():
#         result_lst.append(item)
#     else:
#         result_lst.append(f'{item}_{dictionary[item]}')
#
#     dictionary[item] = dictionary.get(item, 0) + 1  # Если в словаре отсутствует item, то вернётся 0.
#
# print(' '.join(result_lst))  # Склеить все элементы списка через пробел.
# ------------------------------------------------------

# РЕШЕНИЕ 3 ЧЕРЕЗ ПЕРЕЗАПИСЬ СУЩЕСТВУЮЩЕГО СПИСКА:

# lst = input("Введите символы через пробел: ").split()
# dictionary = dict()
#
# for i in range(len(lst)):
#     # Напрямую к значениям списка без range(len()) имеет смысл обращаться, если НЕ планируется их перезапись.
#     # Для перезаписи значений списка требуется обращаться к индексам списка в формате lst[i].
#
#     if lst[i] not in dictionary.keys():
#         dictionary[lst[i]] = 0
#     else:
#         dictionary[lst[i]] += 1
#         lst[i] = f"{lst[i]}_{dictionary[lst[i]]}"
#
# print(*lst)
