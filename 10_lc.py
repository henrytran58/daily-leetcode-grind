#Tues, July 1, 2025
#496. Next Greater Element I
#https://leetcode.com/problems/next-greater-element-i/description/

#FAIL: Couldn't do it myself

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        #[3,4,2,0,1]
        #stack = [3]
        #stack = [4]
        #stack = [4,2]
        #stack = [4,2,0]
        #stack = [4,2]
        
        stack = []
        d = {}
        for n in nums2:
            while stack and n > stack[-1]:
                d[stack.pop()] = n
            stack.append(n)
        for n in stack:
            d[n] = -1
        return [d[x] for x in nums1]