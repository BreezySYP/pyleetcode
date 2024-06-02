# https://leetcode.cn/problems/climbing-stairs/
from functools import cache

class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def dfs(i):
            if i == 0:
                return 1
            if i == 1:
                return 1
            return dfs(i-2)+dfs(i-1)
        return dfs(n)
    

sol = Solution()
print(sol.climbStairs(3))