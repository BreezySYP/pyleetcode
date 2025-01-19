# https://leetcode.cn/problems/minimum-falling-path-sum/
import sys
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[] for i in range(n)]
        dp[0] = matrix[0]
        for i in range(1, n):
            for j in range(n):
                left = dp[i-1][j-1] if j > 0 else sys.maxsize
                mid = dp[i-1][j]
                right = dp[i-1][j+1] if j < n-1 else sys.maxsize
                dp[i].append(min(left,mid,right)+matrix[i][j])
        return min(dp[-1])