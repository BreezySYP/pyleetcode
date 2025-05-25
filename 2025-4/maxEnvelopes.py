# https://leetcode.cn/problems/russian-doll-envelopes/
from bisect import bisect_left
from typing import List


class Solution:

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        g = []
        for x in envelopes:
            j = bisect_left(g, x[1])
            if j == len(g):
                g.append(x[1])
            else:
                g[j] = x[1]
        return len(g)
    
sol = Solution()
print(sol.maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))
print(sol.maxEnvelopes([[1,1],[1,1],[1,1]]))
print(sol.maxEnvelopes([[30,50],[12,2],[3,4],[12,15]]))
print(sol.maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]))
