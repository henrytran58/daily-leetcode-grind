#Wed, July 16, 2025
#844 — Backspace String Compare
#https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        return self.convertString(s) == self.convertString(t)

    def convertString(self, s):
        stack = []

        for ch in s:
            if ch == "#":
                if len(stack) != 0:
                    stack.pop()
            else:
                stack.append(ch)
        
        return "".join(stack)