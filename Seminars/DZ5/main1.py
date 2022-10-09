# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

text = 'абвгдежз иклпрс уфхц эюя туфабвхчш'
s = 'абв'
find = list(filter(lambda x: s not in x, text.split()))
print(find)
