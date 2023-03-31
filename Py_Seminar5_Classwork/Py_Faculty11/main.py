# Проверка палиндрома. Напишите функцию, которая проверяет, является ли строка палиндромом
# (то есть читается одинаково справа налево и слева направо) с использованием рекурсии.
# ------------------------------------------------------

def palindrome(a):
    if len(a) <= 1:
        return print('Это палиндром')
    elif a[0] == a[-1]:
        palindrome(a[1:-1])
    else:
        return print('Это НЕ палиндром')


s = input("Введите строку: ")
palindrome(s)


def is_palindrome(s):
    if len(s) > 1:
        if s[0] == s[-1]:
            return is_palindrome(s[1:-1])
        else:
            return False
    else:
        return True


s = input("Ведите строку: ")

if is_palindrome(s):
    print("Yes")
else:
    print("No")
