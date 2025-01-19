# https://leetcode.cn/problems/maximum-number-of-moves-in-a-grid/
from typing import List

MAX = 10**7
class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        y = len(grid)
        x = len(grid[0])
        dp = [[grid[i][0]] for i in range(y)]
        for j in range(1, x):
            for i in range(y):
                top = dp[i-1][j-1] if i > 0 else MAX
                middle = dp[i][j-1]
                bottom = dp[i+1][j-1] if i < y-1 else MAX
                if min(top, middle, bottom) < grid[i][j]:
                    dp[i].append(grid[i][j])
                else:
                    dp[i].append(MAX)
        # print(dp)

        for i in range(x-1, 0, -1):
            for j in range(y):
                if dp[j][i] != MAX:
                    return i
        return 0
    
sol = Solution()
print(sol.maxMoves([[2,4,3,5],[5,4,9,3],[3,4,2,11],[10,9,13,15]]))