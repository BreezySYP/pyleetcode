from typing import List
from functools import cache


class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        MOD = 1_000_000_007
        n = len(nums)
        f = [[0] * (n + 1) for _ in range(k + 1)]
        f[0][0] = 1
        for i, x in enumerate(nums):
            for j in range(k, x - 1, -1):
                for c in range(1, i+2):
                    f[j][c] = (f[j][c] + f[j - x][c - 1]) % MOD

        ans = 0
        pow2 = 1
        for i in range(n, 0, -1):
            ans = (ans + f[k][i] * pow2) % MOD
            pow2 = pow2 * 2 % MOD
        return ans


        
sol = Solution()
print(sol.sumOfPower([1,2,3], 3))
        
        