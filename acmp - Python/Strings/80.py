"""
Vasya Pupkin's Homework
(Time: 1 sec. Memory: 16 MB)

You are asked to check an arithmetic equation written by Vasya Pupkin as part of his homework.

For example:
- The expression `"2+3=5"` is **correct**.
- The expression `"23*7=421"` is **valid**, but **incorrect**.
- The expressions `"2*=3"`, `"173"`, and `"2+2=a"` are **invalid**.

### Rules:

A **valid expression** must follow this format:
    number operator number = number

Where:
- A **number** is a sequence of one or more decimal digits, optionally preceded by a single minus sign.
- The **operator** must be one of the following: `+`, `-`, `*`, or `/`.
- The equal sign `=` separates the operation and the result.
- There must be **no spaces** in the expression.

If the expression does not conform to this format, it is considered **invalid**.

The goal is to:
- Return `"YES"` if the expression is **valid** and the equality is **mathematically correct**.
- Return `"NO"` if the expression is **valid**, but the equality is **mathematically incorrect**.
- Return `"ERROR"` if the expression is **not valid** at all.

All numbers in the expression are guaranteed to be within the range from -30000 to 30000.
The length of the expression is between 0 and 100 characters.

---

### Input:
The input file **INPUT.TXT** contains a single line with an arithmetic expression string.

---

### Output:
The output file **OUTPUT.TXT** should contain one of the following strings:
- `"YES"` – if the expression is valid and correct;
- `"NO"` – if the expression is valid but incorrect;
- `"ERROR"` – if the expression is not valid.
"""



