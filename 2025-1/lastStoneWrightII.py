from functools import cache
from typing import List

class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        target = sum(stones) / 2
        length = len(stones) / 2

        @cache
        def dfs(i, n):
            if i < 0 or n < 0:
                return 0
            if n < stones[i]:
                return dfs(i-1, n)
            return max(dfs(i-1, n), dfs(i-1, n-stones[i])+stones[i])
        dfs.cache_clear()
        result = abs( sum(stones)  - 2 * dfs(len(stones)-1, target))
        return result

sol = Solution()
print(sol.lastStoneWeightII([2,1]))
