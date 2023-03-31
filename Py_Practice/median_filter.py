# МЕДИАННЫЙ ФИЛЬТР.

def input_float():
    while True:
        f = input('Введите вещественное число: ')
        try:
            return float(f)
        except ValueError:
            print('-> ОШИБКА: Не является вещественным числом!')


def input_natural():
    while True:
        n = input('Введите натуральное число (> 0): ')
        try:
            n = int(n)
            if n > 0:
                return n
            else:
                print('-> ОШИБКА: Не является натуральным числом!')
        except ValueError:
            print('-> ОШИБКА: Не является целым числом!')


def median_filter(n):
    input_list = []
    while True:
        if len(input_list) < n:
            input_list.append(input_float())
        else:
            output_list = input_list.copy()
            print(f"-> Входящие данные:\n{input_list}")
            output_list.sort()
            print(f"-> Отсортированные данные данные:\n{output_list}")
            print(f"-> ВЫВОД:\n{output_list[len(output_list) // 2]}")
            input_list.pop(0)
            print(f"-> Входящие данные после удаления самого старого элемента:\n{input_list}")


median_filter(input_natural())
