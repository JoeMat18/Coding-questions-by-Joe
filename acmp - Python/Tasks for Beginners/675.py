"""
https://acmp.ru/index.asp?main=task&id_task=675

На клеточном поле N•M расположены две жёсткие детали. Деталь A накрывает в каждой строке несколько (не ноль) первых клеток, деталь B — несколько (не ноль) последних; каждая клетка либо полностью накрыта одной из деталей, либо нет.

Деталь B начинают двигать влево, не поворачивая, пока она не упрётся в A хотя бы одной клеткой. Определите, на сколько клеток будет сдвинута деталь B.

Входные данные
В первой строке входного файла INPUT.TXT записано два числа N и M — число строк и столбцов соответственно (1 ≤ N, M ≤ 100). Далее следуют N строк, задающих расположение деталей. В каждой находится ровно M символов "A" (клетка, накрытая деталью A), "B" (накрытая деталью B) или "." (свободная клетка).

Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести одно число — ответ на задачу.
"""

row, col = map(int, input().split())

row_list = [input().strip() for _ in range(row)]


min_dis = float('inf')

for row in row_list:
    A_right_pos = row.rfind('A')
    B_left_pos = row.find('B')

    if A_right_pos != -1 and B_left_pos != -1:
        min_dis = min(min_dis, B_left_pos - A_right_pos - 1)

print(min_dis)



