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
from random import choice

quantity = int(input("Введите количество холодильников (Q): "))
virus_targets = set(input("ВИРУС. Введите номера холодильников для заражения через пробел (N ≤ Q): ").split())

dictionary = "abcdefghijklmnopqrstuvwxyz0123456789"
virus = target = 'ANTON'

titles_list = []
for i in range(quantity):
    title = ''
    for j in range(randint(5, 100)):  # Длина слова в пределах интервала [5, 100].
        title += choice(dictionary)
    titles_list.append(title)

print(titles_list)

for i in range(len(titles_list)):
    if str(i + 1) in virus_targets:
        current_ind = randint(0, len(titles_list[i]))

        for char in virus:
            titles_list[i] = titles_list[i][:current_ind] + char + titles_list[i][current_ind:]
            current_ind = randint(current_ind + 1, len(titles_list[i]))

print(titles_list)
print(f"-> Номера заражённых холодильников:", end="")

word_number = 0
for i in titles_list:

    find = ""
    char = 0
    for j in target:

        flag = True
        while flag and char < len(i):
            if i[char] == j:
                find += i[char]
                char += 1
                flag = False
            else:
                char += 1

    if find == target:
        print(f" {word_number + 1}", end="")
    word_number += 1
