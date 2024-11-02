text = "PythonProgramming"

# text[6:] — начнем с индекса 6 и возьмем до конца строки
result = text[6:]  # "Programming"

# text[:6] — возьмем с начала строки до 6-го индекса (не включая).
result = text[:6]  # "Python"

# text[::2] — берем каждый второй символ от начала до конца строки.
result = text[::2]  # "PtoPormig"

# text[0:10:3] — берем с начала до индекса 10 (не включая) с шагом 3.
result = text[0:10:3]  # "Phg"

# text[-10:-5] — берем с -10 индекса до -5 индекса.
result = text[-10:-5]  # "rogra"

# text[5:1:-1] — берем с индекса 5 до 1 в обратном порядке.
result = text[5:1:-1]  # "ohty"


text = "Python"

# text[-1] — это последний элемент строки "Python", то есть "n".
result = text[-1]  # "n"

# text[-2] — это предпоследний элемент, то есть "o".
result = text[-2]  # "o"

# text[-3:] — срез от третьего элемента с конца до конца строки.
result = text[-3:]  # "hon"

# text[:-3] — срез от начала до третьего элемента с конца (не включая его).
result = text[:-3]  # "Pyt"



text = "Hello, World!"

# Взять подстроку
print(text[0:5])  # "Hello"

# Срез с шагом 2
print(text[0:12:2])  # "Hlo ol"

# Пропустить start или stop
print(text[:5])  # "Hello"
print(text[7:])  # "World!"

# Отрицательные индексы
print(text[-6:])  # "World!"

# Перевернуть строку
print(text[::-1])  # "!dlroW ,olleH"

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Взять подсписок
print(numbers[2:5])  # [3, 4, 5]

# Пропустить каждый второй элемент
print(numbers[::2])  # [1, 3, 5, 7, 9]

# Взять последние 3 элемента
print(numbers[-3:])  # [8, 9, 10]

# Перевернуть список
print(numbers[::-1])  # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
