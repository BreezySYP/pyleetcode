# https://leetcode.cn/problems/longest-increasing-subsequence/
from bisect import bisect_left
from functools import cache
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # @cache
        # def dfs(i: int) -> int:
        #     res = 0
        #     for j in range(i):
        #         if nums[j] < nums[i]:
        #             res = max(res, dfs(j))
        #     return res + 1 
        
        g = []
        for x in nums:
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
        return len(g)
        # return max(dfs(i) for i in range(len(nums)))
                