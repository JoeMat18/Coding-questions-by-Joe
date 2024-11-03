class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        length = 0
        k = len(s) - 1

        while k >= 0 and s[k] == ' ':
            k -= 1 # <=> k = k -1
        
        while k >= 0 and s[k] != ' ':
            length += 1
            k -= 1

        return length