
from bisect import bisect_left
from typing import List


class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        n = len(nums)
       
        suf=[0] * n
        g = []
        for i in range(n-1, 0, -1):
            x = nums[i]
            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            suf[i] = j+1
        
        g = []
        mx = 0
        for i, x in enumerate(nums):

            j = bisect_left(g, x)
            if j == len(g):
                g.append(x)
            else:
                g[j] = x
            pre = j+1
            if pre >= 2 and suf[i] >= 2:
                mx = max(pre + suf[i] - 1, mx)
        return n - mx
    
sol =Solution()
print(sol.minimumMountainRemovals([1,3,1]))
print(sol.minimumMountainRemovals([100,92,89,77,74,66,64,66,64]))