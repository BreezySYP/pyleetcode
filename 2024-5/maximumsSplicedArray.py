#https://leetcode.cn/problems/maximum-score-of-spliced-array/
from typing import List


class Solution:
    def maximumsSplicedArray(self, nums1: List[int], nums2: List[int]) -> int:
        return max(sum(nums2)+self.maxDiffSubArray(nums1, nums2), sum(nums1)+self.maxDiffSubArray(nums2, nums1))

    
    def maxDiffSubArray(self, nums1: List[int], nums2: List[int]):
        dp = [nums1[0] - nums2[0]]
        length = len(nums1)
        for i in range(1, length):
            a = max(dp[i-1], 0) + nums1[i] - nums2[i]
            dp.append(a)
        return max(dp)
    
    

    # def maxSubArray(self, nums: List[int]) -> int:
    #     dp = [nums[0]]
    #     for i in range(1, len(nums)):
    #         a = max(dp[i-1], 0) + nums[i]
    #         dp.append(a)
    #     return max(dp) 
    
    # def minSubArray(self, nums: List[int]) -> int:
    #     dp = [nums[0]]
    #     for i in range(1, len(nums)):
    #         a = min(dp[i-1], 0 ) + nums[i]
    #         dp.append(a)
    #     return min(dp)

