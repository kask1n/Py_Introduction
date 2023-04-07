# Подаем a = [4, 3, -10, 1, 7, 12] —— после преобразования получить список [4, -10, 12, 3, 1, 7]
# ------------------------------------------------------

a = [4, 3, -10, 1, 7, 12]
a.sort(key=lambda x: x % 2)  # Сортировка по остатку от деления, т.е. сначала чётные (0), потом нечётные (1).
print(a)  # [4, -10, 12, 3, 1, 7]
