# Задача №9. Решение в группах.
# По данному целому неотрицательному n вычислите значение n!.
# N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1.
# Решить задачу используя цикл while.
#
# Input: 5
# Output: 120
# ------------------------------------------------------

a = int(input("Введите целое неотрицательное n: "))
factorial = 1

if a < 0:
    print("-> Факториал для отрицательного числа не определён.")
else:
    while a > 1:
        factorial *= a
        a -= 1
    print(f"-> Факториал числа n = {factorial}")