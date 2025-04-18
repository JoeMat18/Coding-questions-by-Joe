"""
Gods' Names and Manuscript Errors
(Time: 1 sec. Memory: 16 MB)

Archaeologists have discovered a collection of ancient manuscript copies containing myths –
various stories about ancient gods. Unfortunately, the scribes who copied these manuscripts
were not very literate and made exactly **one spelling mistake** in each god’s name —
**exactly one character was replaced** with another.

The archaeologists were able to compile:
- A list of the correct names of the gods, and
- A list of all the **suspicious** proper names found in the manuscripts.

However, they are unable to compare these two lists themselves.
Your task is to help them match names from the manuscript to the actual names of the gods,
assuming each suspicious word differs from the correct name by exactly **one character**.

---

### Input

The input file **INPUT.TXT** contains:

- The first line: an integer **N** – the number of god names.
- The next **N** lines: each line contains a name of a god (uppercase Latin letters only).
- Then, a line with integer **M** – the number of suspicious names from the manuscripts.
- The next **M** lines: each line contains a suspicious name (also in uppercase).

Each name (both god names and suspicious words) consists of exactly **K** uppercase letters.
**1 ≤ N, M, K ≤ 30**

---

### Output

The output file **OUTPUT.TXT** must contain **N integers**, separated by spaces.
Each number represents how many suspicious words match the corresponding god's name
with **exactly one character mistake**.

"""

num_of_gods = int(input().strip())
gods = [input().strip() for _ in range(num_of_gods)]
num_of_suspicious_words = int(input().strip())
suspicious_words = [input().strip() for _ in range(num_of_suspicious_words)]
result = [0] * num_of_gods

for k, god in enumerate(gods):
    for word in suspicious_words:
        if len(god) != len(word):
            continue
        if sum(a != b for a, b in zip(god, word)) == 1:
            result[k] += 1
print(*result)