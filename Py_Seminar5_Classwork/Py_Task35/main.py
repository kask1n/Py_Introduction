# Задача №35. Решение в группах.
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым.
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и n(само число).
#
# Input: 5
# Output: yes
# ------------------------------------------------------

flag = True
while flag:
    n = int(input("Введите натуральное число (N≥1): "))
    if n > 0:
        flag = False
    else:
        print("Введено некорректное значение!")


def simple_number(n):
    # for i in range(2, n // 2 + 1):

    i = 2
    while i < (n // 2 + 1):
        if not n % i:  # Все значения кроме 0 возвращают True.
            return print(f"-> Число {n} НЕпростое. Как минимум, делится на {i}.")
        i += 1
    print(f"-> Число {n} простое.")


# simple_number(n)


# def simple(n):
#
#     for i in range(2,n):  # 1 и n(само число)
#         if n % i == 0:
#             return "no"
#     return "yes"

# n = int(input("Введите число: "))
simple_number(n)