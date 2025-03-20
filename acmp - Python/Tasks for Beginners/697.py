"""
https://acmp.ru/index.asp?main=task&id_task=697

Painting the Office
(Time: 1 sec. Memory: 16 MB Difficulty: 11%)

Your favorite uncle is the director of a company that renovates office spaces.
Due to the financial crisis, he decided to optimize his business.

There have been rumors that the foreman in your uncle’s company purchases excess building materials,
using the leftovers to renovate his own summer house.
Your uncle is now interested in finding out the actual number of paint cans required to paint
the walls of an office with dimensions **L** meters in length, **W** meters in width, and **H** meters in height.
One can of paint covers **16 m²**, and for simplicity, the size of doors and windows can be ignored.

Since there are many orders, your uncle asked you to write a program to calculate this.

### Input
The input file **INPUT.TXT** contains a single line with three natural numbers **L, W, H**
separated by spaces – the length, width, and height of the office in meters.
Each number does not exceed **1000**.

### Output
The output file **OUTPUT.TXT** should contain a single integer –
the minimum number of paint cans required to paint all the walls.

"""
import math

l, w, h = map(int, input().split())

s = 2 * h * (w + l)

result = math.ceil(s / 16)

print(result)