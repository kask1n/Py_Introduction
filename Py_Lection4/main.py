import shutil


def f(x):
    return x * x


# a = f  # Переменная a хранит в себе ссылку на функцию f.
# print(f(5))
# print(type(f))
# print(type(a))
# print(a(5))

def calc1(a, b):
    return a + b


def calc2(a, b):
    return a * b


def math(op, x, y):
    print(op(x, y))


# math(calc1, 5, 45)
# math(calc2, 5, 45)

# math(lambda a, b: a + b, 5, 45)  # Пробрасывание лямбда-функции напрямую без промежуточной переменной.
# ------------------------------------------------------

# ЗАДАЧА 1.
# В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар (число; квадрат числа).
# Ввод: 1 2 3 5 8 15 23 38
# Вывод: [(2, 4), (8, 64), (38, 1444)]

data = '1 2 3 5 8 15 23 38'
data = data.split()
data = [int(item) for item in data]


# result = list()
# for item in data:
#     if item % 2 == 0:
#         result.append((item, item ** 2))

# result = [(item, item ** 2) for item in data if not (item % 2)]
# print(result)

def select(func, col):
    return [func(item) for item in col]


def where(func, col):
    return [item for item in col if func(item)]


# result = select(int, data)
result = map(int, data)
print(result)

# result = where(lambda x: x % 2 == 0, result)
result = list(filter(lambda x: x % 2 == 0, result))
print(result)

# result = list(select(lambda x: (x, x ** 2), result))
result = list(map(lambda x: (x, x ** 2), result))
print(result)

list_1 = [index for index in range(1, 20)]
print(list_1)

list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)
# ------------------------------------------------------

# ЗАДАЧА 2.
# С клавиатуры вводится некий набор чисел, в качестве разделителя используется пробел.
# Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

data = '1 2 3 5 8 15 23 38'

# data = data.split()
# data = [int(item) for item in data]
data = list(map(int, data.split()))

print(data)
# ------------------------------------------------------

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)
# ------------------------------------------------------

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data)  # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))  # Функция zip пробегает по минимальному из входящих наборов.
# print(data)  # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]
# ------------------------------------------------------

# towns = ['Казань', 'Смоленск', 'Рыбки', 'Чикаго']
# data = list(enumerate(towns))
# print(data)  # [(0, 'Казань'), (1, 'Смоленск'), (2, 'Рыбки), (2, 'Чикаго')]

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users))
# print(data)  # [(0, 'user1'), (1, 'user2'), (2, 'user3)]
# ------------------------------------------------------

# colors = ['red', '8898', 'blue']
# data = open('file.txt', 'a', encoding='utf-8')
# # Указывается режим, в котором будем работать. Кодировка по умолчанию - utf-8.
# data.writelines(colors)  # Записать данные в файл без разделителей.
# data.close()  # Завершить работу с файлом.

# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 3\n')
#
# print(56)

# path = 'file.txt'
# data = open(path, 'r')
# for line in data:
#     print(line)
# data.close()
# ------------------------------------------------------

# МОДУЛЬ OS.

# import os

# os.chdir(r"E:\Git\2023.03.08_Py_Introduction\Py_Lection3")
# print(os.getcwd())
# print(os.path.basename(r"E:\Git\2023.03.08_Py_Introduction\Py_Lection3\main.py"))
# print(os.path.abspath('main.py'))
# ------------------------------------------------------

# МОДУЛЬ SHUTIL.

# import shutil

# shutil.copyfile(src, dst)  # Копирует БЕЗ МЕТАДАННЫХ содержимое файла src в файл dst.
# shutil.copy(src, dst)  # Копирует содержимое файла src в файл или папку dst.
# shutil.rmtree()
# ОСТОРОЖНО: Удаляет текущую директорию и все поддиректории. Должен указывать на директорию (не ссылку).
