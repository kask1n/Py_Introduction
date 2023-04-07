def show_menu():
    print("\nВыберите необходимое действие:\n"
          "1. Отобразить весь справочник\n"
          "2. Найти абонента по фамилии\n"
          "3. Найти абонента по номеру телефона\n"
          "4. Добавить абонента в справочник\n"
          "5. Сохранить справочник в текстовом формате\n"
          "6. Закончить работу")
    choice = int(input())
    return choice

def read_csv(filename: str):
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data

def print_result(data):
    for i in data:
        for k, v in i.items():
            print(f"{k:10} : {v}")
        print()
    input("Для продолжения нажмите клавишу Enter")

def find_lastname(data):
    lastname = input("Введите фамилию: ")
    for i in data:
        for k, v in i.items():
            if v == lastname:

    input("Для продолжения нажмите клавишу Enter")


choice = show_menu()
phone_book = read_csv("Phonebook/phonebook.csv")

while (choice != 6):
    if choice == 1:
        print_result(phone_book)

    # elif choice == 2:


    # elif choice == 3:


    # elif choice == 4:

    
    # elif choice == 5:

    choice = show_menu()