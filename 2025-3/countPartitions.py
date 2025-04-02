from functools import cache
from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        if sum(nums)<2*k:
            return 0
        
        n=len(nums)
        
        MOD=10**9+7
        @cache
        def dfs (index,tsum):
            if index==len(nums):
                return 1 if tsum<k else 0
            if tsum>=k:
                return 0
            return dfs(index+1,tsum+nums[index])%MOD  + dfs(index+1,tsum)%MOD
        return (pow(2,n)-2*dfs(0,0))%MOD
    
sol = Solution()
print(sol.countPartitions(nums = [1,2,3,4], k = 4))