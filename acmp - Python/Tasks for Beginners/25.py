"""
https://acmp.ru/index.asp?main=task&id_task=25

Одна из основных операций с числами – их сравнение. Мы подозреваем, что вы в совершенстве владеете этой операцией и можете сравнивать любые числа, в том числе и целые. В данной задаче необходимо сравнить два целых числа.

Входные данные
В двух строчках входного файла INPUT.TXT записаны числа A и B, не превосходящие по абсолютной величине 2×109.

Выходные данные
Запишите в выходной файл OUTPUT.TXT один символ "<", если A<B, ">", если A>B и "=", если A=B.
"""

a = int(input().strip())
b = int(input().strip())

if a > b:
    print(">")
elif a < b:
    print("<")
else:
    print("=")