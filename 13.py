



class Solution:
    def romanToInt(self, s: str) -> int:
        # Словарь для римских цифр 
        roman_value = {
            'I': 1, 
            'V': 5, 
            'X': 10, 
            'L': 50, 
            'C': 100, 
            'D': 500, 
            'M': 1000
        }
        total = 0 # Сумма 
        prev_value = 0  # Пред значение

        for char in reversed(s):
            current = roman_value[char]
            if current < prev_value:
                total -= current # <=> total = total - current 
            else: # current >= prev_value
                total += current # <=> total = total + current 
            
            prev_value = current
            
        return total
            



