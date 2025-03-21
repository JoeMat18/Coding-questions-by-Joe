"""
https://acmp.ru/index.asp?main=task&id_task=777

Alarm Clock
(Time: 1 sec. Memory: 16 MB Difficulty: 12%)

The famous explorer Charles F. Muntz, tired after a long journey through the jungle,
went to bed at **10 PM**, setting his alarm for **12 o’clock the next day**.
However, he didn’t manage to sleep for 14 hours – the alarm rang **after just 2 hours**.

Charles forgot that his alarm clock has a **12-hour dial**, and it can only be set
to ring **less than 12 hours** ahead.

### Task
Write a program that determines how many hours the explorer will sleep
before the alarm wakes him up.

### Input
The input file **INPUT.TXT** contains a single line with two integers **S** and **T**
(**1 ≤ S, T ≤ 12; S ≠ T**), separated by a space:
- **S** – the hour when the explorer went to sleep,
- **T** – the hour the alarm is set for (on a 12-hour dial).

### Output
The output file **OUTPUT.TXT** should contain a single integer –
the number of hours the explorer will sleep before the alarm rings.

"""

current_time, waking_up_time = map(int, input().split())

result = (waking_up_time - current_time) % 12

if result == 0:
    print(12)
else:
    print(result)