# Задача №13. Решение в группах.
# Уставшие от необычно теплой зимы, жители решили узнать, действительно ли
# это самая длинная оттепель за всю историю наблюдений за погодой.
# Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями статистики
# за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель.
# Оттепелью они называют период, в который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую синоптикам в работе.
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100).
# В следующих строках располагается N целых чисел.Каждое число – среднесуточная температура
# в соответствующий день. Температуры – целые числа и лежат в диапазоне от –50 до 50.
#
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
# ------------------------------------------------------

from random import randint  # Из библиотеки random подключаем только метод randint.

flag = True
while flag:
    n = int(input("Введите общее количество рассматриваемых дней (N) - не менее 1 и не более 100: "))

    if 0 < n < 101:
        break
    else:
        print("-> Введено некорректное число!")

max_counter = 0
counter = 0

# for i in range(n):  # [0, n). Решение без массива через один цикл.
#     temp = randint(-50, 50)  # [-50; 50]. Если подключаем всю библиотеку, то вызов через random.randint.
#     print(temp, end=" ")  # При наличии end значения выводятся в одну строку.
#
#     if temp > 0:
#         counter += 1
#         if max_counter < counter:
#             max_counter = counter
#     else:
#         counter = 0

statistics = []
for i in range(n):  # [0, n). Решение с массивом через два цикла (заполнение).
    # statistics.insert(i, int(input(f"Введите среднесуточную температуру {i + 1}-го дня: ")))
    statistics.append(int(input(f"Введите среднесуточную температуру {i + 1}-го дня: ")))

for day in statistics:  # Решение с массивом через два цикла (подсчёт результатов).
    if day > 0:
        counter += 1
        if max_counter < counter:
            max_counter = counter
    else:
        counter = 0

print(f"\nКоличество дней самой длинной оттепели: {max_counter}")