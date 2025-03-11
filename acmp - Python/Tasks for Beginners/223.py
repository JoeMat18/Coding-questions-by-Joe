"""
https://acmp.ru/index.asp?main=task&id_task=233

Оргкомитет Московской городской олимпиады решил организовать обзорную экскурсию по Москве для участников олимпиады. Для этого был заказан двухэтажный автобус (участников олимпиады достаточно много и в обычный они не умещаются) высотой 437 сантиметров. На экскурсионном маршруте встречаются N мостов. Жюри и оргкомитет олимпиады очень обеспокоены тем, что высокий двухэтажный автобус может не проехать под одним из них. Им удалось выяснить точную высоту каждого из мостов. Автобус может проехать под мостом тогда и только тогда, когда высота моста превосходит высоту автобуса.

Помогите организаторам узнать, закончится ли экскурсия благополучно, а если нет, то установить, где произойдет авария.

Входные данные
Первая строка входного файла INPUT.TXT содержит число N (1 ≤ N ≤ 1000). Вторая строка содержит N натуральных чисел, не превосходящих 10000, через пробел - высоты мостов в сантиметрах в том порядке, в котором они встречаются на пути автобуса.

Выходные данные
В единственную строку выходного файла OUTPUT.TXT нужно вывести фразу "No crash", если экскурсия закончится благополучно. Если же произойдет авария, то нужно вывести сообщение "Crash k", где k - номер моста, где произойдет авария. Фразы выводить без кавычек ровно с одним пробелом внутри.
"""

BUS_HEIGHT = 437

count_of_bridges = int(input().strip())
bridge_height = list(map(int, input().split()))

for k in range(count_of_bridges):
    if bridge_height[k] <= BUS_HEIGHT:
        print(f"Crash {k+1}")
        break
else:
   print("No crash")