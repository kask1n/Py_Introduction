# Задача №45. Решение в группах.
# Два различных натуральных числа n и m называются
# дружественными, если сумма делителей числа n
# (включая 1, но исключая само n) равна числу m и
# наоборот. Например, 220 и 284 – дружественные числа.
# По данному числу k выведите все пары дружественных
# чисел, каждое из которых не превосходит k. Программа
# получает на вход одно натуральное число k, не
# превосходящее 105. Программа должна вывести все
# пары дружественных чисел, каждое из которых не
# превосходит k. Пары необходимо выводить по одной в
# строке, разделяя пробелами. Каждая пара должна быть
# выведена только один раз (перестановка чисел новую
# пару не дает).
# Ввод:
# ------------------------------------------------------

def find_summ_delitel(num):
    # delitel = []
    summ = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            # delitel.append(i)
            summ += i
    return summ


k = int(input("Введите натуральное число: "))
friends_numbers = {}
for i in range(1, k):
    m = find_summ_delitel(i)
    if find_summ_delitel(m) == i and i != m and m not in friends_numbers.keys():
        friends_numbers[i] = m

print(friends_numbers)


n = int(input("Введите число: "))
def sum_of_proper_divisors(n):
    s = 0
    for k in range(1, n // 2 + 1):
        if n % k == 0:
            s += k
    return s

for i in range(1, 100000):
    j = sum_of_proper_divisors(i)
    if i < j <= n and i == sum_of_proper_divisors(j):
        print(i, j)


def summa_del(n):
    summa = 0
    for i in range(1, n):
        if n % i == 0:
            summa += i
    return summa

k = 300
for i in range(1, k):
    j = summa_del(i)
    if i == summa_del(j) and i < j:
        print(i, j)