# https://leetcode.cn/problems/best-team-with-no-conflicts/

from functools import cache
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        sorted_pairs = sorted(zip(ages, scores))
        ages, scores = zip(*sorted_pairs)

        @cache
        def dfs(i):    
            res = 0
            for j in range(i):
                if scores[j] <= scores[i]:
                    res = max(res, dfs(j))
            return res + scores[i]
        
        return max([dfs(i) for i in range(len(scores))])
        

sol =Solution()
print(sol.bestTeamScore(scores = [1,3,5,10,15], ages = [1,2,3,4,5]))
print(sol.bestTeamScore(scores = [4,5,6,5], ages = [2,1,2,1]))
print(sol.bestTeamScore(scores = [1,2,3,5], ages = [8,9,10,1]))