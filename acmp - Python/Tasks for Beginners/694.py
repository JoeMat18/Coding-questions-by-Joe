"""
https://acmp.ru/index.asp?main=task&id_task=694

Lazy Student Valera
(Time: 1 sec. Memory: 16 MB Difficulty: 21%)

Student Valera is a classic example of a lazy student.
He rarely attends classes and only shows up at the end of the semester to clear his academic debts.
His ultimate dream is to find a single day when he can meet all his professors and pass all his exams at once.

He has a schedule of the professors' availability, which specifies the exact start and end days
each professor is available during the month.

### Task
Help Valera write a program that determines whether there exists a single day
when he can meet all professors and clear his debts.

### Input
The input file **INPUT.TXT** contains:
- The first line contains a natural number **N** – the number of subjects Valera needs to pass (**N ≤ 100**).
- The next **N** lines each contain two integers **A** and **B**, defining the availability range of a professor (**1 ≤ A ≤ B ≤ 31**).

### Output
The output file **OUTPUT.TXT** should contain:
- `"YES"` if there exists a single day when Valera can meet all professors.
- `"NO"` otherwise.

"""

subjects = int(input().strip())

date_table = [0] * 32

for _ in range(subjects):
    a, b = map(int, input().split())
    for k in range(a, b + 1):
        date_table[k] += 1

if (max(date_table) == subjects):
    print("YES")
else:
    print("NO")
