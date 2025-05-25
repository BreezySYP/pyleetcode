# https://leetcode.cn/problems/number-of-longest-increasing-subsequence/
from functools import cache
from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
    
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        cnt = [0] * n
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j])
            dp[i] = dp[i]+1
                

        return dp[n-1]
        

sol =Solution()
print(sol.findNumberOfLIS([1,3,5,4,7]))