#Wed, July 10, 2025
#1313. Decompress Run-Length Encoded List
#https://leetcode.com/problems/decompress-run-length-encoded-list/description/

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(0, len(nums), 2):
            result.extend([nums[i+1]] * nums[i])

        return result
        