# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from random import randint
 
k = int(input('Введите степень k для составления уравнения: '))
list = []
for i in range(k + 1):
    list.append(randint(0, 100))    
    
str = ''
if k == 0:
    str = 'x = 0'
else:
    for i in range(len(list)):
        if i != len(list) - 1 and list[i] != 0 and i != len(list) - 2:
            str += f'{list[i]}x^{len(list) - i - 1}'
            if list [i + 1] != 0:
                str += ' + '
        elif i == len(list) - 2 and list[i] != 0:
            str += f'{list[i]}x'
            if list[i + 1] != 0:
                str += ' + '
        elif i == len(list) - 1 and list[i] != 0:
            str += f'{list[i]} = 0'
        elif i == len(list) - 1 and list[i] == 0:
            str += ' = 0'
 
print(str)