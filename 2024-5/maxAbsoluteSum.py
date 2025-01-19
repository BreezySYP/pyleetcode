# https://leetcode.cn/problems/maximum-absolute-sum-of-any-subarray/
from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        dp_big = [0 if nums[0] < 0 else nums[0]]
        dp_small = [0 if nums[0] > 0 else nums[0]]
        dp = [abs(nums[0])]

        for i in range(1, len(nums)):
            big = max(0, dp_big[i-1]+nums[i])
            dp_big.append(big)
            small = min(0, dp_small[i-1]+nums[i])
            dp_small.append(small)
            dp.append(max(big, abs(small)))
        return max(dp)
    

sol = Solution()
print(sol.maxAbsoluteSum([1,-3,2,3,-4]))