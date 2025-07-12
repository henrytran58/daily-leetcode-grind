#Fri, July 11, 2025
#414. Third Maximum Number
#https://leetcode.com/problems/third-maximum-number/description/

class MySolution:
    def thirdMax(self, nums: List[int]) -> int:
        f_max = nums[0]
        s_max = None
        t_max = None

        for i in range(1, len(nums)):
            if nums[i] == f_max:
                pass
            elif nums[i] > f_max:
                if s_max == None:
                    s_max = f_max
                    f_max = nums[i]
                else:
                    t_max = s_max
                    s_max = f_max
                    f_max = nums[i]
            #else < f_max
            elif s_max == None:
                s_max = nums[i]
            elif nums[i] > s_max:
                t_max = s_max
                s_max = nums[i]
            elif nums[i] == s_max:
                pass
            elif t_max == None or nums[i] > t_max:
                t_max = nums[i]

        return t_max if t_max != None else f_max
    

class aLittleCleanerSolution: #but slower than above
    def thirdMax(self, nums: List[int]) -> int:
        f_max, s_max, t_max = None, None, None
        nums = list(set(nums))

        if len(nums) < 2:
            return nums[0]

        if nums[0] > nums[1]:
            f_max, s_max = nums[0], nums[1]
        else:
            f_max, s_max = nums[1], nums[0]

        for i in range(2, len(nums)):
            if nums[i] == f_max:
                pass
            elif nums[i] > f_max:
                t_max = s_max
                s_max = f_max
                f_max = nums[i]
            #else < f_max
            elif nums[i] > s_max:
                t_max = s_max
                s_max = nums[i]
            elif nums[i] == s_max:
                pass
            elif t_max == None or nums[i] > t_max:
                t_max = nums[i]
                
        return t_max if t_max != None else f_max
    
class SortingSolution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))  # Remove duplicates
        nums.sort(reverse=True) # Sort descending
        if len(nums) >= 3:
            return nums[2]
        return nums[0]