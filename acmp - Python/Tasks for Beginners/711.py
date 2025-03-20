"""
https://acmp.ru/index.asp?main=task&id_task=711

Kart Racing Winner
(Time: 1 sec. Memory: 16 MB Difficulty: 18%)

After another stage of the Formula-A open-wheel racing championship,
the drivers gathered at a café to discuss the results.
They recalled that in their younger years, they competed not in large Formula cars,
but in go-karts – smaller sports cars.

The friends wanted to determine the winner of one of their past kart races.
The winner of the race was the driver with the **lowest total time** across all laps.

Since the final results were not preserved, each of the **n** participants
recalled and wrote down their lap times for each of the **m** laps.
Unfortunately, this information made it difficult for them to manually determine the winner.
So, they asked you to do it for them.

### Task
Write a program that determines the winner of the kart race.

### Input
The input file **INPUT.TXT** contains:
- The first line contains two integers **n** and **m** (**1 ≤ n, m ≤ 100**) –
  the number of participants and the number of laps in the race.
- The next **2∙n** lines describe each participant's performance:
  - The first line contains the participant's name, using only English letters
    (both uppercase and lowercase).
    All names are unique, and uppercase/lowercase letters are considered different.
  - The second line contains **m** positive integers representing the participant’s
    lap times for each of the **m** laps (each number does not exceed **1000**).
  - The length of each name does not exceed **255** characters.

### Output
The output file **OUTPUT.TXT** should contain the name of the winner –
the participant with the lowest total race time.
If multiple participants have the same total time, output **any** of their names.
"""

n, m = map(int, input().split())

the_best_racer = ""
min_time = float('inf')

for _ in range(n):
    name = input().strip()
    lap_times = list(map(int, input().split()))

    total_time = sum(lap_times)

    if min_time > total_time:
        min_time = total_time
        the_best_racer = name
print(the_best_racer)

