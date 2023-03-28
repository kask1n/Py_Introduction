# Перестановка n элементов - упорядоченная (n, n)-выборка без повторений. Размер выборки = n!
#
# from itertools import permutations
#
# string = "1234"
# values = list(permutations(string))
# print(values)
# print(len(values))

def input_float(prompt=None):
    while True:
        s = input(prompt)
        try:
            return float(s)
        except ValueError:
            print('-> ОШИБКА: Ожидалось вещественное число.')

# f = input_float('Введите вещественное число: ')
# print('Вы ввели', f)
