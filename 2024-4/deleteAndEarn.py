# https://leetcode.cn/problems/delete-and-earn/
from collections import Counter
from functools import cache


class Solution:
    # def deleteAndEarn(self, nums: List[int]) -> int:
    def deleteAndEarn(self, nums) -> int:  
        maxvalue = max(nums)
        table = dict(Counter(nums))
        @cache
        def dfs(n):
            if n == 0:
                return getValue(0)
            if n == 1:
                return max(getValue(0), getValue(1))
            return  max( dfs(n-2)+getValue(n), dfs(n-1))
        def getValue(n):
            return table.get(n, 0) * n

        return dfs(maxvalue)
    

sol = Solution()
print(sol.deleteAndEarn([2,2,3,3,3,4]))