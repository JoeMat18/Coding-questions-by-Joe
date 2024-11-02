from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        first_str = strs[0] 
        prefix = ""

        for k in range(len(first_str)):
            current_char = first_str[k] 

            for string in strs[1:]:
                if k >= len(string) or string[k] != current_char:
                    return prefix

            prefix += current_char
        
        return prefix