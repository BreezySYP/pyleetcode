from typing import List


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        arr2.sort()

        n = len(arr1)
        idx = 0
        taken = 0

        for i in range(1, n):
            if arr1[i-1] >= arr1[i]:
                
                if len(arr2) is 0:
                    return -1
                
                for j in range(idx, len(arr2)):
                    if arr2[j] > arr1[i-1]:
                        arr1[i] = arr2[j]
                        taken += 1
                        idx = j
                        break
                    elif j == len(arr2)-1:
                        return -1
                
        return taken
                    

sol = Solution()
print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]))
print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [4,3,1]))
print(sol.makeArrayIncreasing(arr1 = [1,5,3,6,7], arr2 = [1,3,2,4]))
        