"""
https://acmp.ru/index.asp?main=task&id_task=606

Даны длины трех отрезков. Требуется проверить: могут ли они являться сторонами невырожденного треугольника.

Входные данные
Первая строка входного файла INPUT.TXT содержит 3 натуральных числа X Y Z через пробел – длины заданных отрезков. Длины отрезков не превышают 1000.

Выходные данные
В выходной файл OUTPUT.TXT выведите YES, если отрезки могут быть сторонами треугольника и NO в противном случае.
"""

a, b, c = map(int, input().split())

if a + b > c and a + c > b and c + b > a:
    print("YES")
else:
    print("NO")
