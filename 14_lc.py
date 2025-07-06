#Sat, July 5, 2025
#2114. Maximum Number of Words Found in Sentences
#https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/description/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        Max = 0

        for sentence in sentences:
            number_of_words = sentence.count(" ") 
            if number_of_words + 1 > Max:
                Max = number_of_words + 1
        
        return Max