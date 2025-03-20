"""
https://acmp.ru/index.asp?main=task&id_task=757

Ethanol Molecules
(Time: 1 sec. Memory: 16 MB Difficulty: 10%)

Every school student studying organic chemistry is familiar with the molecular formula of ethanol: **C2H5(OH)**.
From this formula, it is clear that one ethanol molecule consists of:
- **2** carbon (C) atoms
- **6** hydrogen (H) atoms
- **1** oxygen (O) atom

### Task
Given the number of available atoms for each of these elements,
determine the **maximum possible number of ethanol molecules** that can be formed.

### Input
The input file **INPUT.TXT** contains a single line with three natural numbers:
- **C** – number of carbon atoms,
- **H** – number of hydrogen atoms,
- **O** – number of oxygen atoms.

All numbers are separated by spaces and do not exceed **10¹⁸**.

### Output
The output file **OUTPUT.TXT** should contain a single integer –
the **maximum number of ethanol molecules** that can be formed from the given atoms.

"""

C, H, O = map(int, input().split())

needed_C = 2
needed_H = 6
needed_O = 1

count_ethanol = min(C // needed_C, H // needed_H, O // needed_O)

print(count_ethanol)
