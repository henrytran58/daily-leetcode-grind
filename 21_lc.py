#Sat, July 12, 2025
#345. Reverse Vowels of a String
#https://leetcode.com/problems/reverse-vowels-of-a-string/description/

class Solution:
    def reverseVowels(self, s: str) -> str:
        result = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}
        v_list = []
        for ch in s:
            if ch in vowels:
                v_list.append(ch)
        
        curr_index = len(v_list) - 1
        for ch in s:
            if ch in vowels:
                result.append(v_list[curr_index])
                curr_index -= 1
            else:
                result.append(ch)
        result = "".join(result)
        return result
