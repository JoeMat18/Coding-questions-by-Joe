"""
https://acmp.ru/index.asp?main=task&id_task=760

Traffic Inspection
(Time: 1 sec. Memory: 16 MB Difficulty: 24%)

Every car owner eventually encounters traffic inspectors.
Your task is to calculate the **minimum** time required for a car to pass a straight section of road
where traffic inspectors are stationed. It is known that all passing vehicles are stopped by the inspectors.

### Assumptions:
- Cars are considered **point objects**, meaning they can instantly stop and resume moving at their maximum speed.
- The car starts at position **0** and ends at position **L**.

### Input
The input file **INPUT.TXT** contains:
- The first line contains three integers:
  - **N** – the number of inspectors (**0 ≤ N ≤ 30**),
  - **V** – the car's maximum speed in km/h (**1 ≤ V ≤ 200**),
  - **L** – the length of the road section in km (**1 ≤ L ≤ 200**).

- The second line contains **N** pairs of integers **xi ti**, where:
  - **xi** – the position of the inspector along the road (**0 ≤ xi ≤ L**),
  - **ti** – the time (in minutes) for which the inspector stops the vehicle (**1 ≤ ti ≤ 10**).

  - All inspectors are positioned at **different** points.

All input values are integers.

### Output
The output file **OUTPUT.TXT** should contain a **floating-point number** representing
the total time required to traverse the road section, measured in **minutes**,
formatted to exactly **two decimal places**.
"""

cops_count, speed, distance = map(int, input().split())

total_time = (distance / speed) * 60

inspector_time = list(map(int, input().split()))

stops_time = sum(inspector_time[k + 1] for k in range(0, len(inspector_time), 2))

total_time = total_time + stops_time
print(f"{total_time:.2f}")

