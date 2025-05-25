# https://leetcode.cn/problems/minimum-operations-to-make-the-array-k-increasing/

from bisect import bisect_left, bisect_right
from functools import cache
from typing import List


class Solution:
    def kIncreasing(self, arr: List[int], k: int) -> int:
        n = len(arr)
    
        def dfs(m):
            g = []
            for i in range(m, n, k):
                x = arr[i]
                j = bisect_right(g, x)
                if j == len(g):
                    g.append(x)
                else:
                    g[j] = x
            return len(g)
        
        sm = sum([dfs(i) for i in range(k)])
        return len(arr) - sm

sol = Solution()
# print(sol.kIncreasing([5,4,3,2,1], 1))
print(sol.kIncreasing(arr = [4,1,5,2,6,2], k = 2))
