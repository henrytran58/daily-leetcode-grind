#Thur, Jun 26, 2025
#167. Two Sum II - Input Array is Sorted
#https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Your solution must use only constant extra space.
        #Brute force: O(1) space but O(n^2) time
        #Target: O(1) space and O(1) time
        #Q: Why is it given us the sorted array?
        #A: 2 pointers

        left = 0
        right = len(numbers) - 1

        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            else:
                right -= 1
        
        return [left + 1, right + 1]


