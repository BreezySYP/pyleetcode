# https://leetcode.cn/problems/maximum-subarray/
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            a = max(dp[i-1], 0) + nums[i]
            dp.append(a)
        return max(dp)
    
sol = Solution()
sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])