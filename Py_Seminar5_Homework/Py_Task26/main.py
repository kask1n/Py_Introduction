# Задача 26: Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8
# ------------------------------------------------------

flag = True
while flag:
    a = input("Введите число (A): ")
    try:
        a = float(a)
        if not a % 1:
            a = int(a)
        flag = False
    except ValueError:
        print('-> ОШИБКА: Введено некорректное значение!')

flag = True
while flag:
    b = input("Введите целое число (B): ")
    try:
        b = int(b)
        flag = False
    except ValueError:
        print('-> ОШИБКА: Введено некорректное значение!')


def power_recursion(number, power):
    if number == 0:
        return 0
    if power == 0:
        return 1
    elif power > 0:
        return number * power_recursion(number, power - 1)
    else:
        return power_recursion(1 / number, -power)


print(f"-> {a} в степени {b} = {power_recursion(a, b)}")
