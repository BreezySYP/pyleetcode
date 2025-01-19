#https://leetcode.cn/problems/partition-equal-subset-sum/description/

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        total = sum(nums)

        if total % 2:
            return False
        total //= 2 
        
        ## 1 0
        ## 6 5 1 0
        ## 17 16 12 11 6 5 1 0
        ## 22 21 17 16 11 10 6 5 17 16 12 11 6 5 1 0
        
        hashSet = set()
        hashSet.add(0)
        hashSet.add(nums[0])

        for i in range(1, n):
            newSet = set()
            for j in hashSet:
                num = j + nums[i]
                if num == total:
                    return True
                else:
                    newSet.add(num)
            hashSet = hashSet.union(newSet)

        return False


sol = Solution()

print(sol.canPartition([1,5,11,5]))
