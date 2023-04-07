# Задача 49: Общее обсуждение.
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные;
# 2. Программа должна сохранять данные в текстовом файле;
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
# (например, имя или фамилию человека);
# 4. Использование функций. Ваша программа не должна быть линейной.
#
# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию,
# и Вы должны реализовать функционал для изменения и удаления данных.
# ------------------------------------------------------

import csv


def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice


def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)

    return data


def display_all():
    for row in reader:
        print(f'Фамилия: {el[0]}\nИмя: {el[1]}\nНомер телефона: {el[2]}\nКомментарий: {el[3]}\n')


def find_last_name():
    last_name = input('Введите фамилию: ')
    for el in filter(lambda x: x[0] == last_name):
        print(f'Фамилия: {el[0]}\nИмя: {el[1]}\nНомер телефона: {el[2]}\nКомментарий: {el[3]}\n')


def find_phone():
    phone = input('Введите номер телефона: ')
    for el in filter(lambda x: x[2] == phone):
        print(f'Фамилия: {el[0]}\nИмя: {el[1]}\nНомер телефона: {el[2]}\nКомментарий: {el[3]}\n')


def add_user():
    with open('phonebook.csv', 'a', encoding='utf-8', newline='') as out_file:
        info = input('Введите данные абонента: ').split(',')
        csv.writer(out_file).writerow(info)


for elem in iter(show_menu(), '6'):
    with open('phonebook.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)

        if elem == 1:
            display_all()
        if elem == 2:
            find_last_name()
        if elem == 3:
            find_phone()
        if elem == 4:
            add_user()
        if elem == 5:
            display_all()
