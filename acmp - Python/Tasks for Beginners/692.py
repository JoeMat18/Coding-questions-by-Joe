"""
https://acmp.ru/index.asp?main=task&id_task=692

Binary Number Check
(Time: 1 sec. Memory: 16 MB Difficulty: 8%)

There is a popular joke among programmers:
- A bad programmer thinks that 1 kilobyte equals 1000 bytes.
- A good programmer believes that 1 kilometer equals 1024 meters.

Many find this joke amusing because, in computing and information technology,
we often encounter values expressed as powers of two, meaning numbers of the form 2^K,
where K is a non-negative integer. Let's call such numbers **binary numbers**.
These include values like 2, 4, 8, 16, 32, and so on.

Indeed, when dealing with memory sizes or screen resolutions,
binary numbers frequently appear due to the way information is stored in a computer's memory.

### Task
You are given an integer **N**. Determine whether it is a binary number.

### Input
The input file **INPUT.TXT** contains a single integer **N**,
which does not exceed 10,000 in absolute value.

### Output
The output file **OUTPUT.TXT** should contain:
- `"YES"` if the number **N** is a binary number.
- `"NO"` otherwise.

"""

num = int(input().strip())

if num <= 0:
    print("NO")
else:
    while num % 2 == 0:
        num //= 2
    print("YES" if num == 1 else "NO")


