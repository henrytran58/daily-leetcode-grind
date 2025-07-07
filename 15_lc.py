#Sun, July 6, 2025
#941. Valid Mountain Array
#https://leetcode.com/problems/valid-mountain-array/

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        if arr[1] <= arr[0]:
            return False

        increasing = True     
        decreasing = False
        for i in range(len(arr) - 1):
            if arr[i + 1] == arr[i]:
                return False
            elif arr[i + 1] > arr[i]:
                if not increasing:
                    return False
            else:
                increasing = False
                decreasing = True
        
        return decreasing
