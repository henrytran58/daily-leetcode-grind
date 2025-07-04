#Fri, July 4, 2025
#567. Permutation of String
# https://leetcode.com/problems/permutation-in-string/description/


class MySolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        table1 = {}
        #construct table1
        for ch in s1:
            if ch not in table1:
                table1[ch] = 1
            else:
                table1[ch] += 1

        table2 = {}
        for i in range(len(s1)):
            ch = s2[i]
            if ch not in table2:
                table2[ch] = 1
            else:
                table2[ch] += 1
        
        curr = 0
        length1 = len(s1)
        length2 = len(s2)
        #for i in range(len(s1), len(s2)):
        while curr + length1 < length2:
            if self.compare(table1, table2):
                return True
            else:
                ch_curr = s2[curr]
                ch_next = s2[curr + length1] 
                if ch_next not in table2:
                    table2[ch_next] = 1
                else:
                    table2[ch_next] += 1
                
                table2[ch_curr] -= 1
                if table2[ch_curr] == 0:
                    del table2[ch_curr]
                curr += 1

        return self.compare(table1, table2)

    def compare(self, table1, table2):
        if len(table1.keys()) != len(table2.keys()):
            return False

        for key in table1.keys():
            if key not in table2:
                return False
            elif table1[key] != table2[key]:
                return False
        
        return True
    

from collections import Counter

class CleanerSolution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)
        if len1 > len2:
            return False

        table1 = Counter(s1)
        table2 = Counter(s2[:len1])

        if table1 == table2:
            return True

        for i in range(len1, len2):
            table2[s2[i]] += 1
            table2[s2[i - len1]] -= 1
            if table2[s2[i - len1]] == 0:
                del table2[s2[i - len1]]
            if table1 == table2:
                return True

        return False
