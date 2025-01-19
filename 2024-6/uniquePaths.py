# https://leetcode.cn/problems/unique-paths/
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[] for i in range(m)]
        dp[0].append(1)
        for i in range(m):
            for j in range(n):
                x = dp[i-1][j] if i > 0 else 0
                y = dp[i][j-1] if j > 0 else 0
                if x == 0 and y == 0:
                    continue
                dp[i].append(x + y) 
        print(dp)
        return dp[-1][-1]

sol = Solution()
sol.uniquePaths(7,3)   
    
