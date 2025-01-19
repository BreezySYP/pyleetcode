# https://leetcode.cn/problems/minimum-path-cost-in-a-grid/
from typing import List


class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dp = [[] for i in range(m)]
        dp[0] = grid[0]

        for i in range(1,m):
            for j in range(n):
                # arr = []
                # for k in range(n):
                #     arr.push(dp[i-1][k] + moveCost[grid[i-1][k]][j])
                costArr = [dp[i-1][k] + moveCost[grid[i-1][k]][j] for k in range(n)]
                dp[i].append(min(costArr) + grid[i][j])

        # print(dp)
        return min(dp[-1])
            
sol = Solution()
sol.minPathCost([[5,3],[4,0],[2,1]], [[9,8],[1,5],[10,12],[18,6],[2,4],[14,3]])