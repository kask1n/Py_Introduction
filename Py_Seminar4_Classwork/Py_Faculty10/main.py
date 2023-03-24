# Создайте программу для игры с конфетами человек против человека.
# Условие задачи:
# На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?
#
# ------------------------------------------------------

from random import randint


def player_input(candies, player):
    while True:
        n = int(input(f"Игрок {player}, введите количество конфет (1≤N≤28): "))
        if 0 < n < 29:
            return n
        print("-> Введено некорректное количество!")


def random_input(candies, player):
    n = randint(1, 28)
    print(f"Рандомайзер вводит количество конфет: {n}")
    return n


def ai_input(candies, player):
    if candies % 29:
        n = candies % 29
    else:
        n = randint(1, 28)
    print(f"Искусственный интеллект вводит количество конфет: {n}")
    return n


# ИГРА БОТ + БОТ* с интелектом
# import random
# sum=int(input("Введите количество конфет: "))
# sum1=0
# step1=0
# step2=0
# step3=0
# i=1
# while sum>0:
#         if sum<=57 and sum>=30:
#             step1=(sum-29)
#             sum=sum-step1
#             print(f"Ход первого игрока:{step1} ")
#             print(f"Остаток конфет: {sum}")
#             print(f"Первый игрок победил!!! ")
#             break
#         else:
#             for i in range (1,28,1):
#                 if sum - i==58:
#                     step3=i
#             if step3>0:
#                 print(f"Ход первого игрока:{step3} ")
#                 sum=sum-step3
#                 print(f"Остаток конфет: {sum}")
#                 sum1=sum1+step3
#             else:
#                 step1=(random.randint(1,28))
#                 print(f"Ход первого игрока:{step1} ")
#                 sum=sum-step1
#                 print(f"Остаток конфет: {sum}")
#                 sum1=sum1+step1
#
#         step2=(random.randint(1,28))
#         print(f"Ход второго игрока:{step2} ")
#         sum=sum-step2
#         print(f"Остаток конфет: {sum}")