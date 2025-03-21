"""
https://acmp.ru/index.asp?main=task&id_task=778

Office
(Time: 1 sec. Memory: 16 MB Difficulty: 18%)

In the summer, Vasya loved looking out the window.
Across from his house was the office of a construction company.
Throughout the entire month, Vasya observed the employees.
For each of the **31 days** in the month, he knows how many employees came to work.

He also knows that **each employee takes exactly 4 days off** during the month.

Now he’s puzzled – how many total employees work in that office?
Write a program to help Vasya figure it out.

### Input
The input file **INPUT.TXT** contains a single line with **31 non-negative integers**.
Each number represents the number of employees who came to the office on that day.
It is guaranteed that the input is valid.

### Output
The output file **OUTPUT.TXT** should contain a single integer –
the **total number of employees** in the office.
It is guaranteed that the answer does not exceed 100.

"""

attendance = list(map(int, input().split()))

total_visit = sum(attendance)

employees = total_visit // 27

print(employees)