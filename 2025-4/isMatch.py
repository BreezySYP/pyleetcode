# https://leetcode.cn/problems/regular-expression-matching/
from functools import cache


class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if p[0] == "*":
            return False

        def equalChar(self, i, j):
            return p[j] == s[i] or p[j] == "."
        
        @cache
        def dfs(i, j):
            if i < 0:
                return dfs(i, j-2) if p[j] == "*" and j > 0 else j < 0
            if j < 0:
                return i < 0
            
            if p[j] == "*" :
                return (dfs(i-1, j) or dfs(i-1, j-2) or dfs(i, j-2)) if equalChar(self, i, j-1) else dfs(i, j-2)
            return dfs(i-1, j-1) if equalChar(self, i, j) else False
        return dfs(len(s)-1, len(p)-1)
        

        

sol = Solution()
print(sol.isMatch("aab", "c*a*b"))
print(sol.isMatch("aaa", "ab*ac*a"))