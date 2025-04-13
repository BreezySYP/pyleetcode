# https://leetcode.cn/problems/find-maximum-removals-from-source-string/
from functools import cache
from typing import List


class Solution:
    def maxRemovals(self, source: str, pattern: str, targetIndices: List[int]) -> int:
        targetSet = set(targetIndices)
        patlen = len(targetIndices)
        @cache
        def dfs(i, j):
            if j < 0:
                count = 0
                for num in targetIndices:
                    if num <= i:
                        count += 1
                    else:
                        break 
                return count
            if i < 0:
                return 0 if j < 0 else -float("inf")
            
         
            hit = 1 if i in targetSet else 0
            
            if source[i] == pattern[j]:
                return max(dfs(i-1, j-1), dfs(i-1, j)+hit)
            return dfs(i-1, j)+hit
        ans = dfs(len(source)-1, len(pattern)-1)
        dfs.cache_clear()
        return ans

    
sol = Solution()
print(sol.maxRemovals(source = "abbaa", pattern = "aba", targetIndices = [0,1,2]))
print(sol.maxRemovals(source = "bcda", pattern = "d", targetIndices = [0,3]))
print(sol.maxRemovals(source = "dda", pattern = "dda", targetIndices = [0,1,2]))
print(sol.maxRemovals(source = "yeyeykyded", pattern = "yeyyd", targetIndices = [0,2,3,4]))
print(sol.maxRemovals("yyey",pattern ="y",targetIndices =[0]))