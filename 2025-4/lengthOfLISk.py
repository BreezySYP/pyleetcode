# https://leetcode.cn/problems/longest-increasing-subsequence-ii/

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int], k: int) -> int:

        n = len(nums)
        g = []

        for i, x in enumerate(nums):
            j = bisect_left(g, x)
            if j == len(g):
                if j == 0 or x - g[-1] <= k:
                    g.append(x)
            elif j == 0 or x - g[j-1] <= k:
                g[j] = x
        return len(g)
    
sol = Solution()
# print(sol.lengthOfLIS([7,4,5,1,8,12,4,7], 5))
print(sol.lengthOfLIS([1,3,3,4], 1))
