# print(5, 8, 6)
# n = None
# n = 1.89
# print(n)

# n = "fddf"
# print(n)

# n1 = "vfdffvd"
# print(n1)

# n = 'fd"vfdffvd"df'
# print(type(n))
# print(n)

# print(5)
# print(5)
# print(5)
# """
# print(5, 8)
# print(5)
# print(5, 9)
# """

# a = 5
# b = 5.89
# c = "hello"

# print(a, "-", b, "-", c)
# print(f"{a} - {b} - {c}")
# print("{} - {} - {}".format(a, b, c))

# print("Введите первое число: ")
# a = int(input())  # Вариант ввода данных с новой строки.
# b = int(input("Введите второе число: "))  # Вариант ввода данных в текущей строке.
# print(a, "+", b, "=", a + b)  # Складываются две строки вместо двух чисел.

# c = 5.89
# print(type(c))
# print(c + "56")  # Ошибка, т.к. float + string не складываются.
# c = str(c)  # Приведенеие данных к целочисленному типу.
# print(type(c))
# print(c + "89")  # ОК, т.к. сложение двух значений типа string.

# c = 1
# print(type(c))
# print(c)
# c = bool(c)
# print(type(c))
# print(c)

# v = "fvdfv"
# v = int(v)

# a = 5.89956
# b = 6.556551
# print(round(a * b, 3))  # Округление результата до первых трёх цифр после запятой.

# iter = 2
# iter += 3  # iter = iter + 3
# iter -= 4  # iter = iter - 4
# iter *= 5  # iter = iter * 5
# iter /= 5  # iter = iter / 5
# iter //= 5  # iter = iter // 5
# iter %= 5  # iter = iter % 5
# iter **= 5  # iter = iter ** 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)
# a = "qwe"
# b = "qwe"
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# username = input("Введите имя: ")
# if username == "Маша":
#     print("Ура, это же МАША!")
# elif username == "Марина":
#     print("Я так ждала Вас, Марина!")
# elif username == "Ильнар":
#     print("Ильнар = топ)")
# else:
#     print("Привет,", username)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# print(summa)  # 9

# i = 0
# while i < 5:
#     # if i == 3:
#     #     break  # Принудительный выход из цикла.
#     i = i + 1
# else:  # Выполняется только при самостоятельном завершении цикла while.
#     print("Пожалуй")
#     print("хватит )")
# print(i)

# n = int(input())
# flag = True
# i = 2
# while flag:  # Нахождение минимального делителя натурального числа.
#     if n % i == 0:  # Если остаток при делении числа n на i равен 0.
#         print(i)
#         flag = False
#     elif i > n // 2:  # Делитель не может превышать введённое число, делённое на 2.
#         print(n)
#         flag = False
#     i += 1

# for i in 1, -2, 3, 14, 5:
#     print(i)  # 1 -2 3 14 5

# r = range(5)  # 0 1 2 3 4
# r = range(2, 5)  # 2 3 4
# r = range(0, -5)  # ----
# r = range(1, 10, 2)  # 1 3 5 7 9
# r = range(100, 0, -20)  # 100 80 60 40 20
# for i in r:
#     print(i)

# for i in "qwerty":
#     print(i)  # q w e r t y

# a = "qwerty"
# print(a[0])  # q

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)  # ***** (5 times)

# text = "СъЕШЬ ещё этих МяГкИх французских булок"
# # print(len(text))  # Позволяет узнать размер коллекции данных.
# print("ещё" in text)  # Есть ли искомое слово в строке (true or false)
# print(text.lower())  # Перевести все символы в нижний регистр.
# print(text.upper())  # Поднять все символы в верхний регистр.
# print(text.replace("ещё", "ЕЩЁ"))  # Заменить одни символы другими.

text = "Съешь ещё этих мягких французских булок"
# print(text[0])  # C
# print(text[1])  # ъ
# print(text[len(text) - 1])  # к
# print(text[-1])  # к
# print(text[-5])  # б
# print(text[:])  # Съешь ещё этих мягких французских булок
# print(text[:2])  # Cъ - как в функции range(2), т.е. [0, 2).
# print(text[len(text) - 2 :])  # ок
# print(text[20:])  # х французских булок
# print(text[2:9])  # ешь ещё
# print(text[6:-18])  # ещё этих мягких - [6, -18), т.е. от 6 до 18 с конца коллекции.
# print(text[0 : len(text) : 6])  # Сеикакл - от 0 до конца коллекции с шагом 6.
# print(text[::6])  # Сеикакл - по умолчанию от начала и до конца коллекции с шагом 6.
text = text[2:9] + text[-5] + text[:2]
print(text)  # ешь ещёбСъ
