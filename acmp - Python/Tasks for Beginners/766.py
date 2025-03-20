"""
https://acmp.ru/index.asp?main=task&id_task=766

Nuts
(Time: 1 sec. Memory: 16 MB Difficulty: 3%)

A squirrel gathered **N** cones with nuts in the forest.
The squirrel was very picky and only collected cones that contained **exactly M nuts**.
It is also known that the squirrel needs **at least K nuts** to survive the winter.

### Task
Determine whether the squirrel has enough nuts for the winter.

### Input
The input file **INPUT.TXT** contains a single line with three natural numbers **N, M, K**, separated by spaces:
- **N** – the number of cones collected (**1 ≤ N ≤ 100**),
- **M** – the number of nuts in each cone (**1 ≤ M ≤ 100**),
- **K** – the minimum number of nuts needed for the winter (**1 ≤ K ≤ 10,000**).

### Output
The output file **OUTPUT.TXT** should contain:
- `"YES"` if the squirrel has enough nuts for the winter.
- `"NO"` otherwise.

"""

n, m, k = map(int, input().split())

if (n * m) < k:
    print("NO")
else:
    print("YES")