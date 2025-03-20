"""
https://acmp.ru/index.asp?main=task&id_task=716

Maxim's Triangle
(Time: 1 sec. Memory: 16 MB Difficulty: 30%)

Since childhood, Maxim has been a talented musician and a skilled craftsman.
Recently, he built a simple percussion instrument – a **triangle**.
Now, he wants to determine the frequency of the sound produced by his instrument.

Maxim has a professional musical tuner that can play notes at specified frequencies.
He follows this process:
- He plays different notes on the tuner.
- For each note, starting from the second one, he determines **by ear**
  whether it is **closer** or **further** from the sound of his triangle than the previous note.
- Maxim has **absolute pitch**, so his judgment is always accurate.

Maxim recorded the frequencies he tested along with his assessment of how close they are to his triangle’s frequency.
It is known in advance that the triangle's frequency is between **30 Hz and 4000 Hz**.

### Task
Write a program that determines the possible range of frequencies at which Maxim's triangle might sound.

### Input
The input file **INPUT.TXT** contains:
- The first line contains an integer **n** – the number of notes Maxim played on the tuner (**2 ≤ n ≤ 1000**).
- The next **n** lines contain Maxim's observations. Each line consists of:
  - A floating-point number **fi** – the frequency set on the tuner in Hertz (**30 ≤ fi ≤ 4000**).
  - A word `"closer"` or `"further"` (starting from the second line):
    - `"closer"` means the current note is closer to the triangle's frequency than the previous one:
      ```
      |fi - f_triangle| < |fi-1 - f_triangle|
      ```
    - `"further"` means the current note is farther from the triangle's frequency than the previous one.
    - If a note is equally distant from the triangle's frequency as the previous note,
      Maxim could have written **either** `"closer"` or `"further"`.

It is guaranteed that Maxim’s observations are **logically consistent**.

### Output
The output file **OUTPUT.TXT** should contain two floating-point numbers,
representing the **minimum and maximum possible values** for the triangle's frequency.
The numbers should be printed with **at least** **six decimal places** of precision.
"""

