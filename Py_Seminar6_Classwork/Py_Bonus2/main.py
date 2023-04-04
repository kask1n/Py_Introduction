# Задача 5.
# Необходимо вывести список в обратном порядке.
# ------------------------------------------------------

def reverse(lst):
    if len(lst) < 1:
        return []
    return [lst[-1]] + reverse(lst[:-1])


list1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(list1)

print(reverse(list1))
