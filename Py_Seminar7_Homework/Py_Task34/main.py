# Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм.
# Поскольку разобраться в его кричалках не настолько просто,
# насколько легко он их придумывает, Вам стоит написать программу.
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе одинаковое.
# Фраза может состоять из одного слова. Если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры.
# В ответе напишите “Парам пам-пам”, если с ритмом всё в порядке и “Пам парам”, если с ритмом не всё в порядке.
#
# Ввод: пара-ра-рам рам-пам-папам па-ра-па-дам
# Вывод: Парам пам-пам
# ------------------------------------------------------

import re


def is_rhyme(vowels_count):
    for index in range(len(vowels_count) - 1):
        if (vowels_count[index]) != (vowels_count[index + 1]):
            return False
    return True


vowels = 'аеёиоуыэюя'
words = 'пара-ра-рам рам-пам-папам па-ра-па-дам'.split()
entries = []

for word in words:
    entries.append(0)
    for char in vowels:
        entries.append(entries.pop() + word.count(char))

print("Список слов:", words)
print("Количество гласных в словах:", entries)
print("-> Парам пам-пам") if is_rhyme(entries) else print("-> Пам парам")

# words = list(filter(lambda x: len(list(re.findall('аеёиоуыэюя', x))), words))
# print("Список слов:", words)

# if find_vowels(lambda x: map(x.count(d), words), words):
#     print('same')
# else:
#     print('different')
