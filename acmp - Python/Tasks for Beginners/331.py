"""
https://acmp.ru/index.asp?main=task&id_task=331

Задано время отправления поезда и время в пути до конечной станции. Требуется написать программу, которая найдет время прибытия этого поезда (возможно, в другие сутки).


Входные данные
Входной файл INPUT.TXT содержит две строки. В первой строке задано время отправления, а во второй строке – время в пути. Время отправления задается в формате «HH:MM», где HH время в часах, которое принимает значение от 00 до 23, ММ – время в минутах, которое принимает значение от 00 до 59. Время в пути задается двумя неотрицательными целыми числами – количество часов и количество минут. Числа разделяются одним пробелом. Количество часов не превышает 120, минут – 59.

Выходные данные
Выходной файл OUTPUT.TXT должен содержать одну строку – время прибытия поезда на конечную станцию. Формат вывода этого времени совпадает с форматом ввода времени отправления.
"""

departure = input().strip()
time_travel = input().strip()

hh, mm = map(int, departure.split(':'))

travel_hours, travel_minutes = map(int,time_travel.split())

mm += travel_minutes
hh += travel_hours + (mm // 60)

mm %= 60 # Оставляем только чистые минуты
hh %= 24 # Учитываем переход на новые сутки

print(f"{hh:02}:{mm:02}")
