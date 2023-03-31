# Задача 28:
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#
# 2 2
# 4
# ------------------------------------------------------

def input_natural_or_zero(text):
    while True:
        x = input(f"Введите целое число ({text}≥0): ")
        try:
            x = int(x)
            if x >= 0:
                return x
            else:
                print('-> ОШИБКА: Введено отрицательное число!')
        except ValueError:
            print('-> ОШИБКА: Введено некорректное значение!')


def summ(first, second):
    if second == 0:
        return first
    return summ(first + 1, second - 1)


a = input_natural_or_zero('A')
b = input_natural_or_zero('B')
print(f"{a} + {b} = {summ(a, b)}")
