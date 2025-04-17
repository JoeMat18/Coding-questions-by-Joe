"""
https://acmp.ru/index.asp?main=task&id_task=780

Football
(Time: 1 sec. Memory: 16 MB Difficulty: 22%)

Instead of doing his homework, Vasya was watching a football match and recording the score
displayed on the scoreboard after each goal.

For example, he might have written down the following sequence:
**1:0, 1:1, 1:2, 2:2, 2:3**.

After that, he **added up all the recorded numbers**:

1 + 0 + 1 + 1 + 1 + 2 + 2 + 2 + 2 + 3 = 15

Using the total sum Vasya obtained, determine the total number of goals scored in the match.

### Input
The input file **INPUT.TXT** contains a single non-negative integer **S** (**0 ≤ S ≤ 1000**)
– the sum of all recorded numbers.

### Output
The output file **OUTPUT.TXT** should contain a single integer –
the **total number of goals** scored in the match.
"""

import math

s = int(input().strip())

result = (-1 + math.sqrt(8 * s + 1)) / 2

print(result)


