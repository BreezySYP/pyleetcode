#https://leetcode.cn/problems/perfect-squares/
from functools import cache
import math

@cache
def dfs(i, s):
    if i == 0:
        return math.inf if s else 0
    if i*i > s:
        return dfs(i-1, s)
    return min(dfs(i-1, s), dfs(i, s-i*i)+1)

class Solution:
    def numSquares(self, n: int) -> int:
        edge = math.isqrt(n)
      
        return dfs(edge, n)

        

    
sol= Solution()
print(sol.numSquares(12))

