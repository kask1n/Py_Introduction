# Задача №37. Решение в группах.
# Дано натуральное число N и последовательность из N элементов.
# Требуется вывести эту последовательность в обратном порядке.
# Примечание. В программе запрещается объявлять массивы и использовать циклы (даже для ввода и вывода).
#
# Input: 2 -> 3 4
# Output: 4 3
# ------------------------------------------------------

def reverse_input(n):  # Рекурсия для последовательности чисел.
    if n == 0:
        return '->'
    k = int(input("Введите число: "))
    return reverse_input(n - 1) + f' {k}'


def reverse_other(a):  # Рекурсия для строки.
    if len(a) == 0:
        return ""
    else:
        return str(reverse_other(a[1:])) + a[0]


number = int(input("Введите количество чисел: "))
print(reverse_input(number))

# number = input("Введите строку: ")
# print(reverse_other(number))
