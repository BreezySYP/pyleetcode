from functools import cache
from math import inf
from typing import List


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        sumtime = sum(time)
        @cache
        def dfs(i, n):
            if i < 0:
                return inf if sumtime - n > n else 0
            if sumtime - n > n:
                return dfs(i-1, n)

            return min(dfs(i-1, n - time[i] - 1)+cost[i], dfs(i-1, n))
        return dfs(n-1, n)
        

sol = Solution()
print(sol.paintWalls(cost = [1,2,3,2], time = [1,2,3,2]))

##输入：cost = [1,2,3,2], time = [1,2,3,2]
# 输出：3
# 解释：下标为 0 和 1 的墙由付费油漆匠来刷，需要 3 单位时间。同时，免费油漆匠刷下标为 2 和 3 的墙，需要 2 单位时间，开销为 0 。总开销为 1 + 2 = 3 。