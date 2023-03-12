# В некоторой школе решили набрать три новых математических класса и оборудовать
# кабинеты для них новыми партами. За каждой партой может сидеть двое учащихся.
# Известно количество учащихся в каждом из трех классов.
# Выведите наименьшее число парт, которое нужно приобрести для них.

# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32
# ------------------------------------------------------------------------------

class1 = int(input("Введите количество учащихся в классе 1: "))
class2 = int(input("Введите количество учащихся в классе 2: "))
class3 = int(input("Введите количество учащихся в классе 3: "))

# import math
# result = math.ceil(class1 / 2) + math.ceil(class2 / 2) + math.ceil(class3 / 2)

# result = ((class1 // 2 + (class1 % 2 != 0)) +
#           (class2 // 2 + (class2 % 2 != 0)) +
#           (class3 // 2 + (class3 % 2 != 0)))

result = (class1 + 1) // 2 + (class2 + 1) // 2 + (class3 + 1) // 2

print(f"-> Наименьшее требуемое число парт для трёх классов: ", result)
