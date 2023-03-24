# Задача №25. Решение в группах.
# Напишите программу, которая принимает на вход строку и отслеживает, сколько раз
# каждый символ уже встречался. Количество повторов добавляется к символам с помощью постфикса формата _n.
#
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию .split()
# ------------------------------------------------------
import abc

list = input("Введите символы через пробел: ").split()
print(*list)
dict = {}
for i in list:
    if i not in dict:
        dict.update({i: 1})
    else:
        dict[i] += 1
    print(f"{i}_{dict[i]} ", end="")

# string = input('Введите строку: ').split()
# letter_dict = {}
# result_string = []
# for letter in string:
#     if letter in letter_dict.keys():
#         result_string.append(f'{letter}_{letter_dict[letter]}')
#     else:
#         result_string.append(letter)
#     letter_dict[letter] = letter_dict.get(letter, 0) + 1
#
# print(' '.join(result_string))


# list = input("Введите строку: ").split()
# dict = dict()
#
# for i in range(len(list)):
#     if list[i] in dict.keys():
#         dict[list[i]] += 1
#         list[i] = (f"{list[i]}_{str(dict[list[i]])}")
#     else:
#         dict[list[i]] = 0
#
# print(list)