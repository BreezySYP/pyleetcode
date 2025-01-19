# https://leetcode.cn/problems/combination-sum-iv/


from functools import cache


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        @cache
        def dfs(n):
            if n == 0:
                return 1
            return sum(dfs(n-num) for num in nums if num <= n)
        return dfs(target)

# sol = Solution()
# print(sol.combinationSum4([1,2,3], 4))