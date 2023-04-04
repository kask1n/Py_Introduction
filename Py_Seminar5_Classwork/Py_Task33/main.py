# Задача №33. Решение в группах.
# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1
# ------------------------------------------------------

from random import randint

flag = True
while flag:
    n = int(input("Введите количество оценок (N≥1): "))
    if n > 0:
        flag = False
    else:
        print("Введено некорректное значение!")

list1 = [randint(1, 5) for _ in range(n)]
print(*list1)

max_score = max(list1)
min_score = min(list1)

print(max_score)
print(min_score)

for i in range(n):
    if list1[i] == max_score:
        list1[i] = min_score

print(*list1)
