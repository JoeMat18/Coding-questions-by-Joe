"""
https://acmp.ru/index.asp?main=task&id_task=755

Strawberry Picking
(Time: 1 sec. Memory: 16 MB Difficulty: 6%)

Masha and Misha went strawberry picking.
Masha managed to pick **X** berries, while Misha picked **Y** berries.
Since the strawberries were delicious, they might have eaten some of them.
According to our estimates, together they ate **Z** berries.

### Task
Determine the total number of berries they originally picked.
Additionally, check whether our calculations about the eaten berries are reasonable
(they should not have eaten more berries than they had picked).

### Input
The input file **INPUT.TXT** contains a single line with three natural numbers **X, Y,** and **Z**
(**1 ≤ X, Y, Z ≤ 1000**), separated by spaces.

### Output
The output file **OUTPUT.TXT** should contain:
- The **total number of berries picked**, if the calculations are reasonable.
- The word `"Impossible"` if the reported number of eaten berries exceeds the total picked amount.

"""

x, y, z = map(int, input().split())

result = (x + y) - z

if result < 0:
    print("Impossible")
else:
    print(result)