# https://leetcode.cn/problems/unique-paths-ii/
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[] for i in range(m)]
        dp[0].append(1)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                x = dp[i-1][j] if i > 0 else 0
                y = dp[i][j-1] if j > 0 else 0
                dp[i].append(x + y if obstacleGrid[i][j] == 0 else 0) 
        return dp[-1][-1]
    
sol = Solution()
sol.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])   