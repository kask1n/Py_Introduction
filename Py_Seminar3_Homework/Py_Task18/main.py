# Задача 18: В массиве A[1...N] требуется найти самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка выводит самый близкий элемент к X.
# Input N: 5
# Output: 1 2 3 4 5
# Input X: 6
# Output: -> 5
# ------------------------------------------------------

from random import randint

n = int(input("Введите количество элементов: "))
a = []
for i in range(n):
    a.insert(i, randint(1, 9))
print(*a)
x = int(input("Введите искомый элемент: "))
res = 0
dif = 0
while not res:
    for i in a:
        if abs(x - i) == dif:
            res = i
    dif += 1

print(f"Самый близкий по величине элемент к заданному числу {x}: {res}")


from random import randint
a = []
n = int(input("Введите количество числе в списке:  "))
x = int(input("Искомое число:  "))
for i in range(n):
    a.append(randint(1,10))
print(a)
j = 0
find_res = 0
flag = True
while find_res == 0:
    i = 0
    while i<n and flag:
        if abs(x-a[i])==j:
            find_res = a[i]
            flag = False
        i+=1
    j+=1

print(f'res = {find_res}')