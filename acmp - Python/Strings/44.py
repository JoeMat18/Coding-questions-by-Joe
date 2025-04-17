"""

Arrows
(Time limit: 1 sec. Memory limit: 16 MB Difficulty: 20%)
You are given a sequence consisting only of the characters '>', '<' and '-'. Find out the number of arrows hidden in this sequence. Arrows are substrings of the form '>>-->' and '<--<<'.

Input
The first line of input contains no more than 250 characters '>', '<' and '-' without spaces. The first line may or may not end with newline character(s).

Output
Output one integer equal to the number of arrows.
"""


s = input().strip()

count = 0

arrow_r = '>>-->'
arrow_l = '<--<<'

for k in range(len(s) - 4):
    if s[k: k+5] == arrow_r or s[k:k+5] == arrow_l:
        count += 1
print(count)