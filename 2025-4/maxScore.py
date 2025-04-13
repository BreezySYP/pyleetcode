# https://leetcode.cn/problems/maximum-multiplication-score/
from functools import cache
from typing import List


class Solution:
    def maxScore(self, a: List[int], b: List[int]) -> int:

        @cache
        def dfs(i, j):
            if j < 0:
                return 0
            if i < 0:
                return -float("inf")
            return max(dfs(i-1, j), dfs(i-1, j-1)+a[j]*b[i])
        ans = dfs(len(b)-1, len(a)-1)
        dfs.cache_clear() 
        return ans