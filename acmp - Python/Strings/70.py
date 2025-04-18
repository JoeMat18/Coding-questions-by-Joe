"""
String Power and Root
(Time: 1 sec. Memory: 16 MB)

Let a string be defined as `s = s₁s₂...sₙ`.
The **k-th power** of string `s` (for `k > 0`) is a string `sᵏ` formed by concatenating `s` with itself `k` times.
For example, the 3rd power of the string `"abc"` is `"abcabcabc"`.

The **k-th root** of a string `s` (for `k > 0`) is a string `t` such that `tᵏ = s`.
If no such string exists, we say the root does not exist.

### Task
Write a program that, given a string `s` and an integer `k ≠ 0`, performs:
- If `k > 0`: compute the **k-th power** of `s`.
- If `k < 0`: compute the **|k|-th root** of `s` (i.e., check whether such a string exists and output it).

If the resulting string is longer than **1023 characters**, output only the **first 1023 characters**.
If the root does **not exist**, output `"NO SOLUTION"`.

### Input
The input file **INPUT.TXT** contains:
- First line: a non-empty string `s` (lowercase English letters only, with length ≤ 1000),
- Second line: an integer `k` (**k ≠ 0**, **|k| < 100001**).

### Output
The output file **OUTPUT.TXT** should contain the resulting string as described above.

"""


s = input().strip()
k = int(input().strip())
MAX_OUT = 1023

if k > 0:
    total_len = len(s) * k
    if total_len <= MAX_OUT:
        print(s * k)
    else:
        times = MAX_OUT // len(s) + 1
        print((s * times)[:MAX_OUT])

else:
    k_abs = abs(k)
    if len(s) % k != 0:
        print("NO SOLUTION")
    else:
        part_len = len(s) // k_abs
        t = s[:part_len]
        if t * k_abs == s:
            print(t)
        else:
            print("NO SOLUTION")
