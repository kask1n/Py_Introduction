# Задача 2:
# Найдите сумму цифр трехзначного числа.

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)
# --------------------------------------

year = int(input("Введите год: "))
if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    # Скобки для двух булевых выражений под and НЕобязательны, т.к. сначала выполняется and, а потом or.
    print("-> YES (год високосный)")
else:
    print("-> NO (год НЕ високосный)")