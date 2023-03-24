# Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
# В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введённого пользователем слова.
# Будем считать, что на вход подается только одно слово,
# которое содержит либо только английские, либо только русские буквы.
#
# Ввод: ноутбук
# Вывод: 12
# ------------------------------------------------------

import re

# word = input("Введите слово: ").upper()
word = str.upper(input("Введите слово: "))

# scrabble = {1: 'AEIOULNSTRАВЕИНОРСТ',
#             2: 'DGДКЛМПУ',
#             3: 'BCMPБГЁЬЯ',
#             4: 'FHVWYЙЫ',
#             5: 'KЖЗХЦЧ',
#             8: 'JXШЭЮ',
#             10: 'QZФЩЪ'}
#
# scrabble_reverse = {'A': 1, 'E': 1, 'I': 1, 'O': 1, 'U': 1, 'L': 1, 'N': 1, 'S': 1, 'T': 1, 'R': 1,
#                     'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
#                     'D': 2, 'G': 2, 'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
#                     'B': 3, 'C': 3, 'M': 3, 'P': 3, 'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
#                     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4, 'Й': 4, 'Ы': 4,
#                     'K': 5, 'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
#                     'J': 8, 'X': 8, 'Ш': 8, 'Э': 8, 'Ю': 8,
#                     'Q': 10, 'Z': 10, 'Ф': 10, 'Щ': 10, 'Ъ': 10}

dictionary = {'[AEIOULNSTRaeioulnstr]': '1', '[DGdg]': '2', '[BCMPbcmp]': '3',
              '[FHVWYfhvwy]': '4', '[Kk]': '5', '[JXjx]': '8', '[QZqz]': '10',
              '[АВЕИНОРСТавеинорст]': '1', '[ДКЛМПУдклмпу]': '2', '[БГЁЬЯбгёья]': '3',
              '[ЙЫйы]': '4', '[ЖЗХЦЧжзхцч]': '5', '[ШЭЮшэю]': '8', '[ФЩЪфщъ]': '10'}

# score = 0
# for char in word:  # РЕШЕНИЕ ЧЕРЕЗ ДВА ЦИКЛА
#     for key in scrabble:  # Вместо запроса ключей и значений можно обратиться к значениям через ключи.
#         if char in scrabble[key]:  # Вместо for и if можно сразу указывать if.
#             score += key
#
# for char in word:  # РЕШЕНИЕ ЧЕРЕЗ ОДИН ЦИКЛ
#     score += scrabble_reverse.get(char, 0)  # При отсутствии в словаре ключа возвращает 0.
#
# print(f"-> Ценность введённого слова = {score}")

for key in dictionary:
    word = re.sub(key, dictionary[key], word)  # TODO: Разобраться в работе функции re.sub.

print(f"-> Ценность введённого слова = {sum(map(int, word))}")  # TODO: Разобраться в работе функции map.
