"""
https://acmp.ru/index.asp?main=task&id_task=685

Golden Sand
(Time: 1 sec. Memory: 16 MB Difficulty: 10%)

Employees of a factory that produces golden sand from air decided to improve their financial situation.
They sneaked into the factory's warehouse, where golden sand of three types was stored.
They could sell one kilogram of the first type of golden sand for A1 rubles,
the second type for A2 rubles, and the third type for A3 rubles.

However, they had only three containers:
- The first container could hold up to B1 kilograms of sand,
- The second container could hold up to B2 kilograms,
- The third container could hold up to B3 kilograms.

They needed to fill all containers completely to maximize their total earnings.
The rules for filling the containers are as follows:
1. Different types of sand cannot be mixed in one container.
2. A single type of sand cannot be split across multiple containers.

Write a program that determines the maximum amount of money the employees can earn
by optimally filling the containers with golden sand.

### Input
The input file INPUT.TXT contains a single line with six natural numbers:
A1, A2, A3, B1, B2, B3, separated by spaces.
All numbers do not exceed 100.

### Output
The output file OUTPUT.TXT should contain a single integer –
the maximum amount of money the employees can earn.

"""

sand_type1, sand_type2, sand_type3, containers1, containers2, containers3 = map(int, input().split())

sorted_sand = sorted([sand_type1, sand_type2, sand_type3], reverse=True)
sorted_containers = sorted([containers1, containers2, containers3], reverse=True)

result = sum(sorted_containers[k] * sorted_sand[k] for k in range(3))

print(result)



