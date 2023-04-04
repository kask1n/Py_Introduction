# Задача 3
# Дан список чисел. Превратите его в список квадратов этих чисел.
#
# ------------------------------------------------------

lst = [1, 2, 3, 4, 5, 6, 7, 8]

for item in lst:
    print(str(item).rjust(4), end="")

print()
lst = list(map(lambda x: x ** 2, lst))

for item in lst:
    print(str(item).rjust(4), end="")
