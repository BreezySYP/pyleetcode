# https://leetcode.cn/problems/target-sum/description/
from functools import cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if (total + target) % 2:
            return 0
        
        t = (total + target) / 2
        length = len(nums)

        @cache
        def dfs(n, w):
            if n < 0:
                return 0 if w != 0 else 1
            if w < nums[n]:
                return dfs(n-1, w)
            return dfs(n-1, w) + dfs(n-1, w-nums[n])
        return dfs(length-1, t)
        
        
sol = Solution()
print(sol.findTargetSumWays([1,1,1,1,1], 3)) # 5