# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# ------------------------------------------------------

from random import randint


def input_natural():
    while True:
        x = input(f"Введите начальное количество конфет: ")
        try:
            x = int(x)
            if x > 0:
                return x
            else:
                print('-> ОШИБКА: Количество должно быть больше нуля!')

        except ValueError:
            print('-> ОШИБКА: Введено некорректное значение!')


def select_player(x):
    while True:
        n = int(input(f"Выберите режим {x}-го игрока (1 - человек, 2 - рандомайзер, 3 - ИИ): "))
        if 0 < n < 4:
            return n
        print("-> Введено некорректное значение!")


def player_input(candies):
    while True:
        n = int(input(f"Введите количество конфет (1≤N≤28): "))
        if 0 < n < 29 and n <= candies:
            return candies - n
        print("-> Введено некорректное количество!")


def random_input(candies):
    n = randint(1, min(candies, 28))
    print(f"-> Рандомайзер вводит количество конфет: {n}")
    return candies - n


def ai_input(candies):
    if candies % 29:
        n = candies % 29
    else:
        n = randint(1, min(candies, 28))
    print(f"-> Искусственный Интеллект вводит количество конфет: {n}")
    return candies - n


candies = input_natural()
p1_type = select_player(1)
p2_type = select_player(2)
print("ИГРА НАЧАЛАСЬ!\n")

first = True
while candies > 0:

    if first:
        player_type = p1_type
        turn = 1
    else:
        player_type = p2_type
        turn = 2

    print(f"Осталось конфет: {candies}\nХод игрока {turn}. ", end="")

    if player_type == 1:
        candies = player_input(candies)
    elif player_type == 2:
        candies = random_input(candies)
    else:
        candies = ai_input(candies)

    first = not first

    if not candies:
        print(f"ПОБЕДИЛ ИГРОК {turn}!")
