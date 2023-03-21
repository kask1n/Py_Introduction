# Задача №17. Решение в группах.
# Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения списка или список задан изначально.
# ------------------------------------------------------

# a = [1, 1, 2, 0, -1, 3, 4, 4]
# print(len(set(list_1)))
# i = 0
# j = 1
#
# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             a.pop(i)
# print(len(a))


mass = input().split()
new_mass = []
for i in mass:
    if i not in new_mass:
        new_mass.append(i)
count = len(new_mass)
print(count)
#
# print(len(set(input("Введите числа через запятую: ").split(','))))
