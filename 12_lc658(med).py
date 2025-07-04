#Thur, July 3, 2025
#658. Find K Closest Elemenets
#https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        head = 0
        tail = len(arr) - 1
        while tail - head >= k:
            a = arr[head]
            b = arr[tail]

            if self.aIsCloser(a, b, x):
                tail -= 1
            else:
                head += 1

            
        return arr[head:(tail+1)]

    def aIsCloser(self, a, b, x):
        if abs(a - x) > abs(b - x):
            return False
        elif abs(a - x) < abs(b - x):
            return True
        else:
            return a < b

class MostOptimalSolution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            if x - arr[mid] > arr[mid + k] - x:
                left = mid + 1
            else:
                right = mid

        return arr[left:left + k]
