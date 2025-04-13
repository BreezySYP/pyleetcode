# https://leetcode.cn/problems/distinct-subsequences/
from functools import cache


class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        @cache 
        def dfs(i, j):
            if j < 0:
                return 1
            if i < j:
                return 0
            if s[i] == t[j]:
                return dfs(i-1, j) + dfs(i-1,j-1)
            return dfs(i-1, j)
        return dfs(len(s)-1, len(t)-1)