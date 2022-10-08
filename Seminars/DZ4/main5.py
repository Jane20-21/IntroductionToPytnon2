# Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий
# сумму многочленов.
# Пример:
# файл1: 2x^2 + 7x + 5
# файл2: 4x^2 + 3x + 9
# результат: 6x^2 + 10x + 14

ur1 = '4*x**3 + 2*x**2 + 2*x + 2'
ur2 = '6*x**3 + 5*x**2 + 4*x + 5'

ur1 = ur1.split(' + ')
ur2 = ur2.split(' + ')

res = ''
for i in range(len(ur1) - 1):
    if i < len(ur1) - 2:
        arg1 = ur1[i].split('*')
        arg2 = ur2[i].split('*')
        arg_sum = str(int(arg1[0]) + int(arg2[0]))
        arg_ur = arg_sum + arg1.pop(1) + '^' + arg1.pop(2) + ' + '
        res += arg_ur
    elif i == len(ur1) - 2:
        arg1 = ur1[i].split('*')
        arg2 = ur2[i].split('*')
        arg_sum = str(int(arg1[0]) + int(arg2[0]))
        arg_ur = arg_sum + arg1.pop(1) + ' + '
        res += arg_ur

res += str(int(ur1[3]) + int(ur2[3]))
print(res)
