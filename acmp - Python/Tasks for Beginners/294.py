"""
https://acmp.ru/index.asp?main=task&id_task=294

Вновь созданная фирма купила заброшенные склады на окраине города. Новому заведующему складами поручили произвести учёт в короткие сроки. Всё шло хорошо, пока случайно не рассыпали контейнеры с болтами и гайками на каждом складе, после чего собрали их в общие (для болтов и гаек) контейнеры, потеряв при этом несколько деталей.

Помогите оценить нанесённый ущерб на каждом складе, приняв во внимание, что, помимо потерянных деталей, болт (или гайка) считается непригодным, если он не имеет соответствующей гайки (или болта).

Входные данные
Во входном файле INPUT.TXT описано текущее положение на складе. В первой строке через пробел записаны три целых числа: k1, l1, m1 – начальное число болтов (100 ≤ k1 ≤ 30000, k1 кратно 100), процент потерянных деталей (0 ≤ l1 ≤ 100) и стоимость одного болта (1 ≤ m1 ≤ 100) соответственно. Во второй строке через пробел записаны также три целых числа: k2, l2, m2 – начальное число гаек (100 ≤ k2 ≤ 30000, k2 кратно 100), процент потерянных деталей (0 ≤ l2 ≤ 100) и стоимость одной гайки (1 ≤ m2 ≤ 100) соответственно.

Выходные данные
В выходной OUTPUT.TXT выведите одно целое число – размер ущерба
"""

k1, l1, m1 = map(int, input().split())
k2, l2, m2 = map(int, input().split())

lost_bolts = (k1 * l1) // 100
lost_nuts = (k2 * l2) // 100

remaining_bolts = k1 - lost_bolts
remaining_nuts = k2 - lost_nuts

damage = (lost_bolts * m1) + (lost_nuts * m2)

if remaining_bolts > remaining_nuts:
    damage += (remaining_bolts - remaining_nuts) * m1
else:
    damage += (remaining_nuts - remaining_bolts) * m2

print(damage)