#Mon, July 7, 2025
#520. Detech Capital
#https://leetcode.com/problems/detect-capital/description/

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_cap = True if word[0].isupper() else False
        all_lower = True
        for ch in word[1:]:
            if not ch.isupper():
                all_cap = False
            else:
                all_lower = False
        
        return all_lower or all_cap
