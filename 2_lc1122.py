# Mon Jun 23, 2025
# 1122. Relative Sort Array
# https://leetcode.com/problems/relative-sort-array/description/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # [6, 8, 8, 17, 22, 28, 44]
        #         0   1   2  3
        # arr2 = [22, 28, 8, 6] 
        copy_arr1 = list(arr1)
        freq = {}

        for elem in arr1:
            if elem not in freq:
                freq[elem] = 1
            else:
                freq[elem] += 1

        print(freq)
        result = []

        for elem in arr2:
            for i in range(freq[elem]):
                result.append(elem)
                copy_arr1.remove(elem)
        
        copy_arr1.sort()
        result.extend(copy_arr1)

        return result
    


#better approach
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)  # Clean and efficient
        result = []

        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]  # Remove so we don’t process again

        # Remaining elements not in arr2
        remaining = []
        for num in freq:
            remaining.extend([num] * freq[num])

        return result + sorted(remaining)