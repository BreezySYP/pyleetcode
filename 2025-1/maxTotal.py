from functools import cache
from typing import List
import itertools


class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        length = len(rewardValues)
       
        rewardValues.sort()
        
        # 1 0   
        # if 

        hashSet = set()
        hashSet.add(0)
        hashSet.add(rewardValues[0])

        for i in range(1, length):
            newSet = set()
            for j in hashSet:
                if rewardValues[i] > j:
                    newSet.add(rewardValues[i]+j)
            hashSet = hashSet.union(newSet)

        return max(hashSet)
    
sol = Solution()
print(sol.maxTotalReward([1,6,4,3,2]))