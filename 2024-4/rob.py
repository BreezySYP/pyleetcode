# https://leetcode.cn/problems/house-robber/
from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        i = len(nums)
        @cache
        def dfs(n):
            if n == 1:
                return max(nums[:2])
            if n == 0:
                return nums[0]
            return max(dfs(n-1), dfs(n-2)+nums[n])
        return dfs(i-1)