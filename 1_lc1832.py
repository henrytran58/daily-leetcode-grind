# Sun, Jun 22, 2025
# 1832. Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/description/

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet_set = set()
        count = 0
        for letter in sentence:
            if letter not in alphabet_set:
                count += 1
                alphabet_set.add(letter)
        return count == 26
    
    