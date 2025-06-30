#Sun, Jun 29, 2025
#680. Valid Palindrome II
#https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return True
        elif s[0] == s[-1]:
            return self.validPalindrome(s[1:-1])
        else:
            return self.validPalindromeDeleted(s[1:len(s)]) or self.validPalindromeDeleted(s[0:-1])
    
    

    def validPalindromeDeleted(self, s):
        if len(s) == 1 or len(s) == 0:
            return True
        elif s[0] != s[-1]:
            return False
        else:
            return self.validPalindromeDeleted(s[1:-1])