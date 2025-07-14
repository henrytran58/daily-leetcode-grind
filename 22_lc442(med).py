#Sunday, July 14, 2025
#442. Find All Duplicates in an Array
#https://leetcode.com/problems/find-all-duplicates-in-an-array/


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        #manipulate nums => add the number appearing twice to the result without using a list/hashmap/...
        #import note: the bound is [1, n] => n = len(nums)
        #bits manipulation? 
        # 01 01 10 in range [01, 11]
        # if sort the array => the solution will be O(nlogn) time and O(1) space
        # 01 01 10 => 01 XOR 01 => 00 decreases
        # 01 XOR 10 => 11 increase => 11 XOR 11 => 00 decrease
        # => we can't do XOR here?

        # [1, 2, 1]
        # => [1]
        # 1 => [2, 1]
        # [1, 1, 2] => sum will 4, if there's no duplicate, what will the sum be?
        # [1, 2, 3] => 6 => the difference is 2

        # [1, 2, 3, 2] => 10, sum is 8
        # the difference is also 2, can we find the missing number in O(1) space?
        # => no?

        # [1, 2, 1, 4] 

        # Solution Trick: mark the visited spot by multiple the visited place by -1
        result = []

        for i in range(len(nums)):
            curr = nums[i]
            if nums[abs(curr) - 1] < 0:
                result.append(abs(curr))
            else:
                nums[abs(curr) - 1] *= -1
        
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] *= -1
        
        return result


