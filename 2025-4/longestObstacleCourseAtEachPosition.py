# https://leetcode.cn/problems/find-the-longest-valid-obstacle-course-at-each-position/
from bisect import bisect_right
from functools import cache
from typing import List


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        ans = []
        g = []
        for x in obstacles:
            j = bisect_right(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            ans.append(j + 1)
        return ans

    
    

sol =Solution()
# print(sol.longestObstacleCourseAtEachPosition([1,2,3,2]))
print(sol.longestObstacleCourseAtEachPosition([2,2,1]))

# [1,6,7,2,4,5,3]

# i=0, len=1, g1=[1]
# i=1, len=2, g2=[1,6]
# i=2, len=3, g3=[1,6,7]
# i=3, len=4, g2=[1,2]
# i=4, len=5, g3=[1,2,4]
# i=5, len=6, g4=[1,2,4,5]
# i=6, len=7, g3=[1,2,3]

# [g1end, g2end, ..., g4end]
# [1,2,3,5]
