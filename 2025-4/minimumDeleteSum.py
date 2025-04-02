# https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/
from functools import cache


class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m = len(s1)
        n = len(s2)

        @cache
        def dfs(i, j):
            if i < 0:
                return sum([ord(s2[a]) for a in range(j, -1, -1)])
            if j < 0:
                return sum([ord(s1[a]) for a in range(i, -1, -1)])
            if s1[i] == s2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j)+ord(s1[i]), dfs(i, j-1)+ord(s2[j]))
        return dfs(m-1, n-1)