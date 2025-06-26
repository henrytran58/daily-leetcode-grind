# Wed, Jun 25, 2025
# 283. Move Zeroes
# https://leetcode.com/problems/move-zeroes/description/

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        curr = len(nums) - 1
        tail = len(nums) - 1

        while curr >= 0:
            if nums[curr] == 0:
                for i in range(curr, tail):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                tail -= 1
            curr -= 1

        # nums = [0,1,0,3,12]
        # start with nums[4] = 12 => skip
        # nums[3] = 3 => skip
        # nums[2] = 0 => swap nums[2] and nums[3] then nums[3] and nums[4]
    def moveZeroess(self, nums):
        curr = 0
        total_zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[curr] = nums[i]
                curr += 1
            else:
                total_zero += 1
        
        for i in range(total_zero):
            nums[-1-i] = 0
        
    def moveZeroesss(self, nums):

        non_zero = 0  # Pointer for non-zero elements
        
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[non_zero] = nums[non_zero], nums[i]
                non_zero += 1