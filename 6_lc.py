#Fri, Jun 27, 2025
#1365. How Many Numbers Are Smaller Than the Current Number
#https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/description/
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        #Naive: O(n^2)
        # result = []

        # for i in range(len(nums)):
        #     count = 0
        #     for j in range(len(nums)):
        #         if i != j:
        #             if nums[j] < nums[i]:
        #                 count += 1
        #     result.append(count)
        
        # [0, 0, 0, 0, 0, 0, 0,..., 0] 100 slots
        counter = [0] * (max(nums) + 1)
        for i in range(len(nums)):
            counter[nums[i]] += 1
        counting_up = []
        counting_up.append(counter[0])
        for i in range(1, len(counter)):
            counting_up.append(counting_up[i-1] + counter[i])

        # print(counting_up)
        result = []
        for i in range(len(nums)):
            result.append(counting_up[nums[i]] - counter[nums[i]])
        

        return result
                    
