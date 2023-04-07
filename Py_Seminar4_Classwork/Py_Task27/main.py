# Задача №27. Решение в группах.
# Пользователь вводит текст (строку). Словом считается последовательность непробельных символов,
# идущих подряд, слова разделены одним или большим числом пробелов.
# Определите, сколько различных слов содержится в этом тексте.
#
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.
# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells.
# Output: 13
# ------------------------------------------------------

import re

text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure." \
       "# So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells."
print(text)

text = text.lower()  # Перевод всех символов в нижний регистр.
print(text)
# text = text.replace('.', '').replace('#', '')  # Последовательное удаление сначала всех точек, потом решёток.
# text = text.split()  # Преобразование строки в список, где разделителем является пробел (по умолчанию).

text = text.strip('#. ')  # Удаление в начале и в конце строки символов, встречающихся в аргументе.
print(text)

text = re.split(r'[#. \n]+', text)  # Разделение строки по разделителям.
# r - raw (сырые данные); позволяет указывать управляющие последовательности символов, как обычный текст.
# [] - позволяет обращаться не ко всей последовательности внутри, а к любому из символов по отдельности.
# + - позволяет использовать символы как по отдельности, так и в виде последовательности.
print(text)

text = set(text)  # Преобразование списка во множество (с удалением повторяющихся элементов).
print(text)
print(len(text))  # Вывод на экран количества уникальных слов.
