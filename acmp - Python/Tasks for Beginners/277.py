"""
Школьная алгебра


Трёхчлен a + bx + сy от двух переменных x и y однозначно определяется коэффициентами a, b и c. Написать программу, которая по заданным a, b и c выводит соответствующий трёхчлен, записанный с использованием алгебраических соглашений:

коэффициент при члене, содержащем переменную, опускается, если его модуль равен единице;
член, коэффициент при котором равен нулю, опускается (кроме случая, когда все коэффициенты равны нулю, тогда трехчлен состоит из одной цифры 0);
знак "+" опускается, если он предшествует отрицательному коэффициенту;
знак "+" опускается, если он стоит в начале выражения (так называемый унарный плюс);
знак умножения между коэффициентом и переменной опускается.
При этом запрещено менять местами члены.

Входные данные
Во входном файле INPUT.TXT через пробел записаны целые коэффициенты a, b и с, каждое из которых не превосходит 30000 по абсолютной величине.

Выходные данные
Выходной файл OUTPUT.TXT должен содержать трехчлен, записанный с использованием алгебраических соглашений.

"""

a, b, c = map(int, input().split())

result = ""

if a != 0:
    result += str(a)

if b != 0:
    if b > 0 and result:
        result += "+"
    if abs(b) == 1:
        result += "-" if b < 0 else ""
    else:
        result += str(b)
    result += "x"

if c != 0:
    if c > 0 and result:
            result += "+"
    if abs(c) == 1:
        result += "-" if c < 0 else ""
    else:
        result += str(c)
    result += "y"

if not result:
     result = "0"

print(result)




















