"""
https://acmp.ru/index.asp?main=task&id_task=779

Building a School
(Time: 1 sec. Memory: 16 MB Difficulty: 30%)

In the village of Internetovka, all houses are located along one side of a street.
The other side is currently empty, but soon it will be filled with schools, shops, cinemas, and more.

The first project is to build a **school**. The location for the school should be chosen
so that the **total distance** students have to travel from their homes to the school is minimized.

We can represent the village as a number line, where each student's house is located
at an integer coordinate on this line. The school can also be built at any **integer coordinate**,
including the coordinates of existing houses (since it will be on the opposite side of the street).

### Task
Write a program that determines the **optimal coordinate** for the school
based on the known positions of students' houses.

If there are multiple answers, choose the **largest** one.

### Input
The input file **INPUT.TXT** contains:
- The first line: an integer **N** – the number of students (**1 ≤ N ≤ 100,000**).
- The second line: **N distinct integers**, sorted in strictly increasing order,
  representing the coordinates of students' homes.
  Each coordinate is an integer not exceeding **2×10⁹** in absolute value.

### Output
The output file **OUTPUT.TXT** should contain a single integer –
the coordinate where the school should be built.

If multiple positions yield the same minimal total distance, output the **largest** one.

"""
