class Solution:
    def reverse(self, x: int) -> int:
        
        INT_MAX = 2**31
        INT_MIN = -2**31
        
        reversed_int = 0

        minus = 1 # = -1
        if x < 0:
            minus *= -1
            x_abs = abs(x) # 123 
        else:
            x_abs = x


        while x_abs != 0:
            digit = x_abs % 10 # Извлекаем последнюю цифру # digit = 3
            x_abs = x_abs // 10 # 12

            if reversed_int > INT_MAX // 10 or (reversed_int == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            if reversed_int < INT_MIN // 10 or (reversed_int == INT_MIN // 10 and digit > -(INT_MIN % -10)):
                return 0

            reversed_int = reversed_int * 10 + digit 

        return reversed_int * minus 
        

