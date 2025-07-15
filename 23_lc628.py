#Mon, July 14, 2025
#628. Maximum Product of Three Numbers
#https://leetcode.com/problems/maximum-product-of-three-numbers/

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        first_prod = 1
        sec_prod = 1
        if nums[0] > 0:
            return nums[-1] * nums[-2] * nums[-3]
        else:
            first_prod = nums[0] * nums[1] * nums[-1]
            sec_prod = nums[-1] * nums[-2] * nums[-3]
        
        return first_prod if first_prod > sec_prod else sec_prod

class CleanerSolution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[-1] * nums[-2] * nums[-3],
                   nums[0] * nums[1] * nums[-1])