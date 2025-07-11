#Fri, July 11, 2025
#942. DI String Match
#https://leetcode.com/problems/di-string-match/description/

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        high = len(s)
        low = 0
        result = []
        for ch in s:
            if ch == "I":
                result.append(low)
                low += 1
            else:
                result.append(high)
                high -= 1
        
        result.append(high)
        return result