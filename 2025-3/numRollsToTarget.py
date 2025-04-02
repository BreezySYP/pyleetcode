#https://leetcode.cn/problems/number-of-dice-rolls-with-target-sum/
from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        if not (n <= target <= n * k):
            return 0  # 无法组成 target
        MOD = 1_000_000_007
        @cache
        def dfs(i, j, s):
            if j == 0:
                return 0
            if i == 0:
                return 1 if s == 0 else 0
            if target < j:
                return dfs(i, j-1, s) % MOD
            return dfs(i, j-1, s) % MOD + dfs(i-1, k, s-j) % MOD
        return dfs(n, k, target) % MOD
    
sol = Solution()
print(sol.numRollsToTarget(n = 2, k = 6, target = 7))