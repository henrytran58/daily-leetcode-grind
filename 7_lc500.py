#Sat, Jun 28, 2025
#500. Keyboard Row
#https://leetcode.com/problems/keyboard-row/description/

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p"]
        second_row = ["a", "s", "d", "f", "g", "h", "j", "k", "l"]
        third_row = ["z", "x", "c", "v", "b", "n", "m"]
        rows = [set(first_row), set(second_row), set(third_row)]
        result = []
        for word in words:
            word_lower = word.lower()
            first_char = word_lower[0]
            if first_char in rows[0]:
                r = 0
            elif first_char in rows[1]:
                r = 1
            else:
                r = 2
            # print(r)
            add = True
            for i in range(1, len(word)):
                if word_lower[i] not in rows[r]:
                    add = False
                    break
            if add:
                result.append(word)

        return result