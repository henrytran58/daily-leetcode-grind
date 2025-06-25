#Tue Jun 24, 2025
#136. Single Number
#https://leetcode.com/problems/single-number/

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0

        for n in nums:
            result ^= n

        return result