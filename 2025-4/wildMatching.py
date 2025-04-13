# https://leetcode.cn/problems/wildcard-matching/
from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n = len(s)
        m = len(p)
        @cache
        def dfs(i, j):
            if j < 0:
                return i < 0
            if i < 0:
                return dfs(i, j-1) if p[j] == "*" else j < 0
            if p[j] == "*":
                return dfs(i-1, j) or dfs(i, j-1) or dfs(i-1, j-1)
            if p[j] == "?" or p[j] == s[i]:
                return dfs(i-1, j-1)
            return False

        return dfs(n-1, m-1)
        

sol = Solution()
print(sol.isMatch(s ="adceb", p ="*a*b"))