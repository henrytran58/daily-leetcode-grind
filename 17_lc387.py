#Tues, July 8, 2025
#387. First Unique Character in a String
#https://leetcode.com/problems/first-unique-character-in-a-string/description/

class Solution:
    def firstUniqChar(self, s: str) -> int:
        table = {}

        for ch in s:
            if ch not in table:
                table[ch] = 1
            else:
                table[ch] += 1
        
        for index in range(len(s)):
            if table[s[index]] == 1:
                return index
        
        return -1