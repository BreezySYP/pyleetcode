# https://leetcode.cn/problems/shortest-common-supersequence/
from functools import cache


class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        @cache
        def dfs(i, j):
            if i < 0:
                return str2[:j+1]
            if j < 0:
                return str1[:i+1]
            
            if str1[i] == str2[j]:
                return dfs(i-1, j-1)+str1[i]
            
            left = dfs(i-1, j) + str1[i]
            right = dfs(i, j-1) + str2[j]
            return right if len(left) > len(right) else left
        return dfs(n-1, m-1)

sol = Solution()
print(sol.shortestCommonSupersequence(str1 = "abac", str2 = "cab"))
print(sol.shortestCommonSupersequence(str1 = "aaaaaaaa", str2 = "aaaaaaaa"))