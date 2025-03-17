"""
http://acmp.ru/index.asp?main=task&id_task=539

На свой день рождения Петя купил красивый и вкусный торт, который имел идеально круглую форму. Петя не знал, сколько гостей придет на его день рождения, поэтому вынужден был разработать алгоритм, согласно которому он сможет быстро разрезать торт на N равных частей. Следует учесть, что разрезы торта можно производить как по радиусу, так и по диаметру.

Помогите Пете решить эту задачу, определив наименьшее число разрезов торта по заданному числу гостей.

Входные данные
Входной файл INPUT.TXT содержит натуральное число N – число гостей, включая самого виновника торжества (N ≤ 1000).

Выходные данные
В выходной файл OUTPUT.TXT выведите минимально возможное число разрезов торта.
"""

guests = int(input().strip())

if guests == 1:
    print(0)
elif guests % 2 == 0:
    print(guests // 2)
else:
    print(guests)