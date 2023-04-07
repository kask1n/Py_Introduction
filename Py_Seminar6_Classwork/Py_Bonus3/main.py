# Турист собирается в поход. Он сможет нести N (кг) вещей.
# Но вещей, которые он запланировал уложить в рюкзак, оказалось намного больше.
# Нужно определить, какие вещи от наиболее тяжелых к самым легким поместятся в рюкзак.
#
# Пример ввода:
# 10
#
# Пример вывода:
# палатка
# спальный мешок
# удочка
# термос
# салфетки
# жвачка
#
# ------------------------------------------------------

things = {'зажигалка': 20, 'компас': 100, 'фрукты': 500, 'рубашка': 300,
          'термос': 1000, 'аптечка': 200, 'куртка': 600, 'бинокль': 400, 'удочка': 1200,
          'салфетки': 40, 'бутерброды': 820, 'палатка': 5500, 'спальный мешок': 2250, 'жвачка': 10}

# backpack = int(input("Введите допустимый вес рюкзака (кг): ")) * 1000
backpack = 10000
print()

while backpack > 0:
    key, value = max(filter(lambda x: x[1] <= backpack, things.items()), key=lambda x: x[1])
    print(key)
    backpack -= things.pop(key)
# ------------------------------------------------------

# things = dict(sorted(things.items(), key=lambda item: item[1], reverse=True))  # Сортировка словаря.
#
# summ = 0
# for key, value in things.items():
#     if value <= backpack - summ:
#         summ += value
#         print(key)
