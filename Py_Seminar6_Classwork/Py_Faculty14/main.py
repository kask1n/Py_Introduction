# 5. Напишите функцию triangle(a, b, c), которая принимает на вход три длины отрезков и определяет,
# можно ли из этих отрезков составить треугольник.
#
# Входные данные: triangle(1, 1, 2)
# Выходные данные: Это НЕ треугольник
# Входные данные: triangle(7, 6, 10)
# Выходные данные: Это треугольник
#
# ------------------------------------------------------

def input_natural(num):
    while True:
        n = input(f'Введите длину {num}-го отрезка (> 0): ')
        try:
            n = int(n)
            if n > 0:
                return n
            else:
                print('-> ОШИБКА: Не является натуральным числом!')
        except ValueError:
            print('-> ОШИБКА: Не является целым числом!')


def check_triangle(segments):
    for index in range(len(segments)):
        if segments[index] >= segments[index - 1] + segments[index - 2]:
            return False
    return True


# def check_triangle_and(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return True
#     return False


segments_list = [input_natural(each) for each in range(1, 4)]  # [1, 3)
print(segments_list)

if check_triangle(segments_list):
    print("-> Это треугольник.")
else:
    print("-> Это НЕ треугольник.")
