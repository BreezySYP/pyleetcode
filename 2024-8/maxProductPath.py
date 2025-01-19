from typing import List

MOD = 10**9 + 7

class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        min_arr = [[0] * m for _ in range(n)]
        max_arr = [[0] * m for _ in range(n)]
        min_arr[0][0] = max_arr[0][0] = grid[0][0]
        for i in range(1, n):
            max_arr[i][0]  = min_arr[i][0] = grid[i][0] * min_arr[i-1][0]
        for j in range(1, m):
             max_arr[0][j] = min_arr[0][j] = grid[0][j] *  min_arr[0][j-1]

        for i in range(1,n):
            for j in range(1,m):
                c = grid[i][j]
                max_arr[i][j] = max( max_arr[i][j-1] * c, max_arr[i-1][j] * c, min_arr[i][j-1] * c, min_arr[i-1][j]* c )
                min_arr[i][j] =  min( max_arr[i][j-1] * c, max_arr[i-1][j] *c , min_arr[i][j-1]*c, min_arr[i-1][j] *c )
        # print(max_arr)
        # print(min_arr)
        return max_arr[-1][-1] % MOD if max_arr[-1][-1] >=0 else -1
    
sol=Solution()
sol.maxProductPath([[1,4,4,0],[-2,0,0,1],[1,-1,1,1]])