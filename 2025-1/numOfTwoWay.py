# https://leetcode.cn/problems/ways-to-express-an-integer-as-sum-of-powers/description/
from functools import cache
import math

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        
        # plus = 1 if x == 1 else 0
        
        target = math.ceil(n ** (1/x))

        @cache
        def dfs(i, w):
            if i < 1:
                return 0 if w != 0 else 1
            pownum = pow(i, x)
            if pownum > w:
                return dfs(i-1, w)
            return dfs(i-1, w) + dfs(i-1, w-pownum)
        return dfs(target, n) % (10**9 + 7)

sol = Solution()
print(sol.numberOfWays(4, 1))