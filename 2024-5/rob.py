#https://leetcode.cn/problems/house-robber-ii/

from functools import cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        # dp1 = [0 for num in nums]
        # dp2 = [0 for num in nums]
        # dp1[0] = nums[0]
        # dp2[1] = nums[1]
        # for i in range(1, n-1):
        #     dp
        # for j in range(2, n):
        i = len(nums)-1
        if i ==0:
            return nums[0]
        @cache
        def dfs1(n):
            if n == 0:
                return nums[0]
            if n < 0:
                return 0
            return max(dfs1(n-1), dfs1(n-2) + nums[n])
        @cache
        def dfs2(n):
            if n == 1:
                return nums[1]
            if n < 1:
                return 0
            return max(dfs2(n-1), dfs2(n-2) + nums[n])
        return max(dfs1(i-1), dfs2(i)) 
            
