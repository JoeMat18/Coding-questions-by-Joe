"""
https://acmp.ru/index.asp?main=task&id_task=43

Требуется найти самую длинную непрерывную цепочку нулей в последовательности нулей и единиц.

Входные данные
В единственной строке входного файла INPUT.TXT записана последовательность нулей и единиц (без пробелов). Суммарное количество цифр от 1 до 100.

Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести искомую длину цепочки нулей.
"""

num = input().strip()
max_zeros = 0
zeros_count = 0

for k in num:
    if k == '0':
        zeros_count += 1
        max_zeros = max(max_zeros, zeros_count)
    else:
        zeros_count = 0
print(max_zeros)

