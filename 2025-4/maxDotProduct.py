# https://leetcode.cn/problems/max-dot-product-of-two-subsequences/description/

from functools import cache
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        m = len(nums1)
        n = len(nums2)

        @cache
        def dfs(i, j):
            if i < 0 or j < 0:
                return -float('inf')
            
            ij = nums1[i] * nums2[j]
            return max(dfs(i-1, j), dfs(i, j-1), dfs(i-1, j-1) + ij, ij)
        return dfs(m-1, n-1)