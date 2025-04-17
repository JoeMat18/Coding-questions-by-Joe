"""
Bulls and Cows
(Time: 1 sec. Memory: 16 MB Difficulty: 20%)

Petya and Vasya often play logic games. Recently, Petya introduced Vasya
to a new game called "Bulls and Cows", and now they play it constantly.

### Rules:
- Petya thinks of a **four-digit number** consisting of **distinct digits**.
- Vasya tries to guess the number by suggesting different four-digit numbers (also with distinct digits).
- After each guess, Petya gives a clue by telling the number of:
  - **Bulls** – digits that are correct **in both value and position**.
  - **Cows** – digits that are correct **in value** but are **in the wrong position**.

For example, if Petya thinks of the number `5671`, and Vasya guesses `7251`, then:
- Bulls = 1 (digit `1` is in the correct place),
- Cows = 2 (digits `5` and `7` are correct but misplaced).

Although Petya is good at math, even he can make mistakes. Help him by writing a program that,
given Petya’s number and Vasya’s guess, calculates the number of bulls and cows.

### Input
The input file **INPUT.TXT** contains two four-digit natural numbers **A** and **B**
separated by a space:
- **A** – Petya’s secret number,
- **B** – Vasya’s guess.

### Output
The output file **OUTPUT.TXT** should contain two integers separated by a space:
- the number of **bulls**,
- and the number of **cows**.

"""

a_str, b_str = input().split()

bulls = 0
cows = 0

a_list = list(a_str)
b_list = list(b_str)

for k in range(len(a_str)):
    if a_list[k] == b_list[k]:
        bulls += 1
        a_list[k] = b_list[k] = "_" # Not necessary to count this for cow

for k in range(len(b_str)):
    if b_list[k] != "_":
        if b_list[k] in a_list:
            cows += 1
            a_list[a_list.index(b_list[k])] = "_"

print(bulls, cows)