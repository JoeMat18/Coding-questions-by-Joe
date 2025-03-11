"""
https://acmp.ru/index.asp?main=task&id_task=272

Задана последовательность целых чисел. Числа нумеруются по порядку следования, начиная с единицы.

Требуется написать программу, которая найдет сумму максимума из чисел с четными номерами и минимума из чисел с нечетными номерами – max{a2, a4, …}+min{a1, a3, …}.

Входные данные
Входной текстовый файл INPUT.TXT содержит в единственной строке последовательность от 2 до 2×105 целых чисел, которые по модулю не превышают 10000.

Выходные данные
Выходной текстовый файл OUTPUT.TXT должен содержать одно целое число - сумму максимума из чисел с четными номерами и минимума из чисел с нечетными номерами.

"""

nums = list(map(int, input().split()))
max_num = 0
min_num = float('inf')

for k in range(len(nums)):
    if nums[k]  > max_num and nums[k] % 2 == 0:
        max_num = nums[k]
    elif nums[k] < min_num and nums[k] % 2 != 0:
        min_num = nums[k]

print(min_num + max_num)