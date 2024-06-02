#https://leetcode-cn.com/problems/minimum-path-sum/

def minPathSum(grid):
    if grid == None or len(grid) == 0 or grid[0] == None or len(grid[0]) == 0:
        return 0

    lenX = len(grid)
    lenY = len(grid[0])

    dp = [[0 for col in range(lenY)] for row in range(lenX)]
    dp[0][0] = grid[0][0]

    for i in range(1, lenX):
        dp[i][0] += dp[i-1][0] + grid[i][0]

    for i in range(1, lenY):
        dp[0][i] += dp[0][i-1] + grid[0][i]

    for i in range(1, lenX):
        for j in range(1, lenY):
            dp[i][j] = min(dp[i][j - 1], dp[i-1][j]) + grid[i][j]

    return dp[lenX-1][lenY-1]

print(minPathSum([[1,3,1],[1,5,1],[4,2,1]]))