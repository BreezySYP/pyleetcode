##https://leetcode.cn/problems/coin-change-ii/

from functools import cache
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        @cache
        def dfs(i, s):
            if i < 0:
                return 1 if s ==0 else 0
            if s < coins[i]:
                return dfs(i-1, s)
            return dfs(i-1, s) + dfs(i, s-coins[i])
        return dfs(len(coins)-1, amount)