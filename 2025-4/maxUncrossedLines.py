# https://leetcode.cn/problems/uncrossed-lines/
from functools import cache
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return 0
            if nums1[i] == nums2[j]:
                return dfs(i-1, j-1) + 1
            return max(dfs(i-1, j), dfs(i, j-1))
        return dfs(m-1, n-1)
        
sol = Solution()
print(sol.maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]))
