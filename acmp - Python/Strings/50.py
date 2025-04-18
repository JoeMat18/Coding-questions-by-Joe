"""
Substrings
(Time: 1 sec. Memory: 16 MB Difficulty: 29%)

A **cyclic shift** of a string `s` is defined as the string:
`s[k:] + s[:k]` for some integer `k`.
For example, if `s = "abcde"`, then its cyclic shifts include: `"abcde"`, `"bcdea"`, `"cdeab"`, `"deabc"`, `"eabcd"`.

A **substring** of a string `s` is any contiguous sequence of characters from `s`,
i.e., `s[i:j]` for some indices `i` and `j`.

### Task
You are given two strings: `a` and `b`.
Write a program to determine **how many substrings of `a`** are **equal to any cyclic shift** of string `b`.

### Input
The input file **INPUT.TXT** contains:
- First line: string `a` (**1 ≤ |a| ≤ 1000**),
- Second line: string `b` (**1 ≤ |b| ≤ min(100, |a|)**).

Both strings consist only of English letters and digits.

### Output
The output file **OUTPUT.TXT** should contain a single integer –
the number of substrings of `a` that match any cyclic shift of `b`.

### Example
#### Input (INPUT.TXT)
"""

s = input().strip()
b = input().strip()

count = 0
shifts = set()

for k in range(len(b)):
    shifts.add(b[k:] + b[:k])

for k in range(len(s) - len(b) + 1):
    sub_string = s[k:k+len(b)]
    if sub_string in shifts:
        count += 1

print(count)


