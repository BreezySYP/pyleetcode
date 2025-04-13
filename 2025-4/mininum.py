# https://leetcode.cn/problems/sorting-three-groups/
from functools import cache
from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        @cache
        def dfs(i: int) -> int:
            res = 0
            for j in range(i):
                if nums[j] <= nums[i]:
                    res = max(res, dfs(j))
            return res + 1 
        return len(nums) - max(dfs(i) for i in range(len(nums)))