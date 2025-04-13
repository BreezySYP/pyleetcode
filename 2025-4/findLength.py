# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/

from functools import cache
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        f = [[0] * (m + 1) for _ in range(n + 1)]
        for i, x in enumerate(nums1):
            for j, y in enumerate(nums2):
                if x == y:
                    f[i + 1][j + 1] = f[i][j] + 1
        return max(map(max, f))  # 所有 f[i][j] 的最大值
    
sol = Solution()
print(sol.findLength(nums1 = [0,0,0,0,0,0,1,0,0,0], nums2 = [0,0,0,0,0,0,0,1,0,0]))

