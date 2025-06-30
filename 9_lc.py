#Mon, Jun 30, 2025
#1189. Maximum Number Of Balloons
#https://leetcode.com/problems/maximum-number-of-balloons/description/

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        #1 balloon => 1 b, 1 a, 1 n, 2 l, 2 o
        #construct table then divide # l and # 0 by 2
        #take the min
        table = {"b":0, "a":0, "l":0, "o":0, "n":0}

        for ch in text:
            if ch in table:
                table[ch] += 1
        
        table["l"] = table["l"] // 2
        table["o"] = table["o"] // 2

        Min = table["b"]

        for letter in table.keys():
            if table[letter] < Min:
                Min = table[letter]

        return Min