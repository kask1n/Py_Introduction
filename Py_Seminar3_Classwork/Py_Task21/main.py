# Задача №21. Решение в группах.
# Напишите программу для печати всех уникальных значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#         {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально, пользователь его не вводит.
# ------------------------------------------------------

a = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
     {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
s = set()

for i in a:
    s.add(*i.value())
print(*s)

# for i in range(len(a)):
#     for j in range(i + 1, len(a)):
#         if a[i] == a[j]:
#             a.pop(i)

# data = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] #список
# print(data)
# result_set = set()
# for elem in data:
#     for value in elem.values():
#         result_set.add(value.strip())
# print(result_set)