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

# print("123".rjust(5))  # Возвращает строку с выравниванием по правому краю. Заполнитель по умолчанию - пробел.

import re

print(list(re.findall('[яюэыуоиёеа]', 'аеёи00000ыэюя')))  # ['а', 'е', 'ё', 'и', 'ы', 'э', 'ю', 'я']
# Выводит список всех вхождений любого из символов паттерна ПО ОТДЕЛЬНОСТИ в исходной строке.

print(list(re.findall('[яюэыуоиёеа]+', 'аеёи00000ыэюя')))  # ['аеёи', 'ыэюя']
# Выводит список всех вхождений символов КАК ПО ОТДЕЛЬНОСТИ, ТАК И ПОСЛЕДОВАТЕЛЬНОСТЕЙ в исходной строке.

vowels = 'аеёиоуыэюя'
word = 'Пара-ра-рам'
func = lambda i: i in vowels  # Моветон - так обычно не делается.
print(func('я'))
print(list(filter(func, word)))

# ГЕНЕРАТОР СЛОВАРЕЙ:
keys = 'abcde'
vals = [1, 2, 3, 4, 5]
condition = True
resDict = {key: val for (key, val) in zip(keys, vals) if condition}
print(resDict)

resDict = dict(zip(keys, vals))
print(resDict)

vals = range(0, 11, 2)
print(vals)
resDict = {val: val + val for val in vals}
print(resDict)
