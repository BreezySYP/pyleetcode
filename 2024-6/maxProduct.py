# https://leetcode.cn/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dpmin = [nums[0]]
        dpmax = [nums[0]]

        for i in range(1, len(nums)):
            big = max(dpmax[i-1]*nums[i], dpmin[i-1]*nums[i], nums[i])
            small = min(dpmax[i-1]*nums[i], dpmin[i-1]*nums[i], nums[i])
            dpmax.append(big)
            dpmin.append(small)
        
        max(dpmax)

sol = Solution()
sol.maxProduct([2,3,-2,4])