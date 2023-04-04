import re

print(re.sub(r'два', r'три', 'шёл дождь и два студента'))  # 'шёл дождь и три студента'
print(re.sub(r'([a-z]+)( .+)', r'\2 \1', 'python язык программирования'))  # ' язык программирования python'
# \2 — это группа символов ( .+)
# \1 — это группа символов ([a-z]+)