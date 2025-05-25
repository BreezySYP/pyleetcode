# https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/

from typing import List


class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:

        n = len(cuboids)
        for i, x in enumerate(cuboids):
            cuboids[i] = sorted(x)

        cuboids.sort(key=lambda x: (x[0], x[1], x[2]))

        f = [0] * n
        f[0] = cuboids[0][2]

        for i in range(1, n):
            f[i] = cuboids[i][2] 
            for j in range(i):
                if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1] and cuboids[i][2] >= cuboids[j][2]:
                    f[i] = max(f[i], f[j] + cuboids[i][2])
        
        return max(f)
    
sol = Solution()
# print(sol.maxHeight([[7,11,17],[7,17,11],[11,7,17],[11,17,7],[17,7,11],[17,11,7]]))
# print(sol.maxHeight([[35,32,11],[7,6,65],[3,39,41]]))
print(sol.maxHeight([[50,26,84],[2,55,62],[64,63,72]]))