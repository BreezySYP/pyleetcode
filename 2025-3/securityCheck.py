from functools import cache
from typing import List


class Solution:
    def securityCheck(self, capacities: List[int], k: int) -> int:
        
        MOD=1_000_000_007
        caps=[x-1 for x in capacities]
        f=[0]*(k+1)
        f[0]=1
        for x in caps:
            for j in range(k,x-1,-1):
                f[j]=(f[j]+f[j-x])%MOD
        return f[k]
    
sol = Solution()
print(sol.securityCheck(capacities = [2,2,3], k = 2))