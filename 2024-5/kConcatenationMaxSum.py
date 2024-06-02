# https://leetcode.cn/problems/k-concatenation-maximum-sum/
from typing import List


class Solution:
    def kConcatenationMaxSum(self, arr: List[int], k: int) -> int:
       
        max_sub_array =  self.maxSubArray(arr + arr if k > 1 else arr)
        result = 0

        if k > 2:
            sum_total = sum(arr)
            if sum_total > 0:
                max_plus = max(self.sumStart(arr))
                max_minus = sum_total - min(min(self.sumStart(arr)), 0)
                result = max(max_plus + max_minus + (k - 2) * sum_total, max_sub_array)
            else:
                result= max_sub_array
        else:
            result= max_sub_array
        return result % (10**9+7)

                
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]]
        for i in range(1, len(nums)):
            a = max(dp[i-1], 0) + nums[i]
            dp.append(a)
        return max(max(dp), 0)
    
    def sumStart(self, arr: List[int]) -> int:
        sum_pre = 0
        sum_sub = []
        for i in range(len(arr)):
            sum_sub.append(sum_pre+ arr[i])
            sum_pre+=arr[i]
        return sum_sub
    

sol = Solution()
print(sol.kConcatenationMaxSum([-1,-2], 7))

    