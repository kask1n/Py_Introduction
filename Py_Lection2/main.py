# list_1 = []  # Создание пустого списка.
# list_1 = list()  # Создание пустого списка.
# list_1 = [1, 2, 3, 8]
# print(list_1[0])  # 7
# print(*list_1)  # Вывести на экран все значения.
#
# for i in list_1:
#     print(i)
#
# print(len(list_1))  # Вывести на экран количество элементов списка (длину).
# print(list_1[3])  # 8 - элемент с индексом 3.
# print(list_1[-1])  # 8 - первый элемент с конца списка.
# print(list_1[-2])  # 3 - первый элемент с конца списка.
#
# list_1 = [1, 5]
# print(list_1)
# list_1.append(8)  # Добавление элемента в конец списка.
# print(list_1)
# list_1.append(85)
# print(list_1)

# list_1 = []
# print(list_1)
# for i in range(5):
#     list_1.append(i)
#     print(list_1)

# Удаление последнего элемента списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop())  # Удаление последнего элемента списка (0).
# print(list_1)  # [12, 7, -1, 21]
# print(list_1.pop())  # Удаление последнего элемента списка (21).
# print(list_1)  # [12, 7, -1]
# print(list_1.pop())  # Удаление последнего элемента списка (-1).
# print(list_1)  # [12, 7]
# a = list_1.pop()  # Возвращение последнего элемента списка (7) в переменную a.
# print(a)  # 7
# print(list_1)  # [12]

# Удаление конкретного элемента из списка:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0))  # 12
# print(list_1)  # [7, -1, 21, 0]
# print(list_1.pop(1))  # -1
# print(list_1)  # [7, 21, 0]

# Добавление элемента на нужную позицию:
# list_1 = [12, 7, -1, 21, 0]
# print(list_1)
# print(list_1.insert(2, 11))  # Добавление элемента "11" в индекс 2.
# print(list_1)  # [12, 7, 11, -1, 21, 0]

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0])  # 1
# print(list_1[1])  # 2
# print(list_1[-1])  # 10
# print(list_1[-5])  # 6
# print(list_1[:])  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2])  # Индексы [0; 2), т.е. элементы [1, 2]
# print(list_1[len(list_1) - 2:])  # [9, 10]
# print(list_1[2:9])  # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18])  # []
# print(list_1[0:len(list_1):6])  # [1, 7]
# print(list_1[::6])  # [1, 7]
#
# t = ()  # Создание пустого кортежа.
# print(type(t))  # <class 'tuple'>
# print(t)  # ()
# t = (1,)
# print(type(t))  # <class 'tuple'>
# print(t)  # (1,)
# t = (1)
# print(type(t))  # <class 'int'>
# print(t)  # 1
# t = (28, 9, 1990)
# print(type(t))  # <class 'tuple'>
# print(t)  # (28, 9, 1990)

# v = [1, 8, 9]
# print(type(v))  # <class 'list'>
# print(v)  # [1, 8, 9]
# v = tuple(v)
# print(type(v))  # <class 'tuple'>
# print(v)  # (1, 8, 9)

# a, b = 1, 2  # То же, что и: a = 1, b = 2
# a = b = 1  # То же, что и: a = 1, b = 1
# a, b, c = v
# print(a, b, c)

t = (1, 2, 3, 5,)
# print(t[1])  # 2
#
# for i in t:
#     print(i)  # 1 2 3 5
#
# for i in range(len(t)):
#     print(t[i])  # 1 2 3 5

# t = [1, 2, 3, 5, ]
# t[0] = 2
# print(t)  # [2, 2, 3, 5]

# d = {}
# d = dict()
# d['q'] = 'qwerty'
# print(d)  # {'q': 'qwerty'}
# d['w'] = 'werty'
# print(d)  # {'q': 'qwerty', 'w': 'werty'}
# print((d['q']))  # qwerty

# dictionary = {}
# dictionary = {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary)  # {'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# # print(dictionary['left'])  # ←
# # print(dictionary['up'])  # ↑
# # dictionary['left'] = '⇐'
# # print(dictionary['left'])  # ⇐
# # print(dictionary['type'])  # KeyError: 'type'
# del dictionary['left']  # Удаление элемента словаря с ключом 'left'
# # print(dictionary)
#
# dictionary[895] = 98998
# # print(dictionary)  # {'up': '↑', 'down': '↓', 'right': '→', 895: 98998}
#
# # for item in dictionary:  # Цикл для каждого ключа в словаре.
# #     print('{}: {}'.format(item, dictionary[item]))  # Вывод на экран словаря в виде: "Ключ: Значение".
# #     # print(item)  # Вывести на экран все ключи словаря.
# #
# # for (k, v) in dictionary.items():
# #     print(k, v)  # Вывод на экран словаря в виде: "Ключ Значение".
#
# print(dictionary.items())  # Вывод на экран списка, где каждый элемент является кортежем (Ключ, Значение)

# colors = {'red', 'green', 'blue'}
# print(colors)  # {'green', 'blue', 'red'} - при отображении порядок случайный.
# # colors.add('red')
# print(colors)  # {'blue', 'green', 'red'} - при отображении порядок случайный.
# colors.add('gray')
# print(colors)  # {'gray', 'red', 'green', 'blue'} - при отображении порядок случайный.
# colors.remove('red')
# print(colors)  # {'green', 'gray', 'blue'} - при отображении порядок случайный.
# # colors.remove('red')  # KeyError: 'red'
# colors.discard('red')  # OK - Проверка на наличие элемента и после этого запуск .remove
# print(colors)  # {'blue', 'gray', 'green'}
# colors.clear()
# print(colors)  # set()
#
# q = set()

# Операции со множествами в Python:
# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy()  # c = {1, 2, 3, 5, 8}
# u = a.union(b)  # u = {1, 2, 3, 5, 8, 13, 21}
# i = a.intersection(b)  # i = {8, 2, 5}
# dl = a.difference(b)  # dl = {1, 3}
# dr = b.difference(a)  # dr = {13, 21}
# q = a.union(b).difference(a.intersection(b))  # q = {1, 21, 3, 13}
# print(q)

# a = {1, 8, 6}
# b = frozenset(a)  # Замороженное множество.
# print(b)

# list_1 = [exp for item in iterable]  # Добавление элементов в список через цикл.
#           ^ Значение
#                   ^ Индекс
#                           ^ Интервал
# list_1 = [exp for item in iterable( if conditional)]  # Выборка по заданному условию.
#                                        ^ Условие

# Задача: Создать список чисел от 1 до 100:
# list_1 = []
# for i in range(1, 101):  # [1, 101)
#     list_1.append(i)  # Добавление элемента в конец списка.
# print(list_1)  # [1, 2, 3, ... 100]

# list_1 = [i for i in range(1, 101)]
# print(list_1)  # [1, 2, 3, ... 100]
# print(list_1[0])  # 1

# Задача с условием: Только чётные числа.
# list_1 = [i for i in range(1, 101) if i % 2 == 0]  # Проверка остатка от деления.
# print(list_1)  # [2, 4, ... 100]
# list_1 = [(i, i * i) for i in range(1, 11) if i % 2 == 0]  # Добавление кортежа в каждый элемент списка.
# print(list_1)  # [(2, 4), (4, 16), (6, 36), (8, 64), (10, 100)]
# list_1 = [i * 2 for i in range(10) if i % 2 == 0]  # Умножение при добавлении элемента.
# print(list_1)  # [0, 4, 8, 12, 16]

# SyntaxError (Синтаксическая ошибка):
# number_first = 5
# number_second = 7
# if number_first > number_second  # Отсутствует ":"
#     print(number_first)

# IndentationError (Ошибка отступов):
# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first)  # Отсутствует отступ.

# TypeError (Ошибка типов):
# text = 'Python'
# number = 5
# print(text + number)  # Нельзя складывать разные типы (например, строку и число).

# ZeroDivisionError (Деление на ноль):
# number_first = 5
# number_second = 0
# print(number_first // number_second)  # Нельзя делить на ноль.

# KeyError (Ошибка ключа):
# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])  # Такого ключа не существует.

# NameError (Ошибка имени переменной):
# name = 'Ivan'
# print(names)  # Переменной names не существует.

# ValueError (Ошибка значений):
text = 'Python'
print(int(text))  # Символы нельзя привести к целочисленному типу.
