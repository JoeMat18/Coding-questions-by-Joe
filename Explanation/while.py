import unittest

class TestWhileLoop(unittest.TestCase):
    def test_while_simple_count(self):
        # Пример 1: Счетчик с while
        count = 0
        result = []
        while count < 5:  # Пока count меньше 5, выполняем цикл
            result.append(count)
            count += 1  # Увеличиваем count на 1
            #print(f"count {count}")

    def test_while_sum_until_limit(self):
        # Пример 2: Суммируем числа, пока сумма не превысит 10
        total = 0
        num = 1
        while total <= 10:  # Пока total меньше или равен 10
            total += num
            num += 1
            #print (f"total: {total}, num: {num}")
    
    def test_while_infinite_loop_break(self):
        # Пример 3: Бесконечный цикл, прерываемый break
        count = 0
        while True:  # Бесконечный цикл
            count += 1
            if count >= 3:  # Прерываем цикл, если count становится больше или равен 3
                break
            #print(f"count: {count}")

    def test_while_with_decrement(self):
        # Пример 4: Используем while для обратного отсчета
        countdown = 10
        result = []
        while countdown > 0:  # Пока countdown больше 0
            result.append(countdown)
            countdown -= 1  # Уменьшаем countdown на 1
            print(f"countdown: {countdown}")

if __name__ == "__main__":
    unittest.main()
