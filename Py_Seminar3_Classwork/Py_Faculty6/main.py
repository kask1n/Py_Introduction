# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников.
# Теперь он использует их в качестве серверов "Пегого дудочника".
# Помогите владельцу фирмы отыскать все заражённые холодильники.
# Для каждого холодильника существует строка с данными,
# состоящая из строчных букв и цифр, и если в ней присутствует слово "anton"
# (необязательно рядом стоящие буквы, главное наличие последовательности букв),
# то холодильник заражён и нужно вывести номер холодильника, нумерация начинается с 1.
#
# Формат Входных данных:
# В первой строке подаётся число n – количество холодильников.
# В последующих n строках вводятся строки, содержащие латинские строчные буквы и цифры,
# в каждой строке от 5 до 100 символов.
#
# Формат ВЫходных данных:
# Программа должна вывести номера заражённых холодильников через пробел.
# Если таких холодильников нет, то ничего выводить не нужно.
#
# Sample Input 1: 6
# 222anton456 a1n1t1o1n1 0000a0000n00t00000o000000n gylfole richard ant0n
# Sample Output 1: 1 2 3
# Sample Input 2: 9
# osfjwoiergwoignaewpjofwoeijfnwfonewfoignewtowenffnoeiwowjfninoiwfen anton aoooooooooontooooo
# elelelelelelelelelel ntoneeee tonee 253235235a5323352n25235352t253523523235oo235523523523n
# antoooooooooooooooooooooooooooooooooooooooooooooooooooon unton
# Sample Output 2: 1 2 7 8
# ------------------------------------------------------

from random import randint

quantity = int(input("Введите количество холодильников: "))
# dict = "abcdefghijklmnopqrstuvwxyz0123456789"
dict = "aannttoo3"
# list_1 = [exp for item in quantity]
line_1 = []
target = 'anton'

for i in range(quantity):
    word_1 = ''
    for j in range(randint(10, 19)):  # randint[] range[) randint(5,99)
        word_1 += dict[randint(0, len(dict) - 1)]
    line_1.append(word_1)

print(line_1)
find = ""

word_number = 0

for i in line_1:
    # for word in line_1:
    find = ""
    char = 0
    for j in target:
        while char < len(i):
            if i[char] == j:
                find += i[char]
                char += 1
                break
            char += 1
        # break
    if find == target:
        print(f"Номер слова: {word_number + 1}")
    word_number += 1
