# https://leetcode.cn/problems/triangle/
import sys
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)
        dp = [[] for i in range(depth)]
        dp[0].append(triangle[0][0])

        for d in range(1, depth):
            for w in range(d+1):
                left = dp[d-1][w-1] if w > 0 else sys.maxsize
                right = dp[d-1][w] if w < d else sys.maxsize
                dp[d].append(min(left, right)+triangle[d][w])
                
        return min(dp[-1])
    
sol = Solution()
sol.minimumTotal([[2],[3,4],[6,5,7],[4,1,8,3]])