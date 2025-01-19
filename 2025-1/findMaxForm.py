# https://leetcode.cn/problems/ones-and-zeroes/
from functools import cache
from typing import List

# m count of 0
# n count of 1
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeroone = []
        for str in strs:
            arr = [0, 0]
            for c in str:
                if c == '0':
                    arr[0] += 1
                else:
                    arr[1] += 1
            zeroone.append(arr)
    

        @cache
        def dfs(i, number1, number0):
            if i < 0:
                return 0
            if zeroone[i][0] > number0 or zeroone[i][1] > number1:
                return dfs(i-1, number1, number0)
            else:
                return max(dfs(i-1, number1, number0), dfs(i-1, number1-zeroone[i][1], number0-zeroone[i][0])+1)
            
        return dfs(len(zeroone)-1, n, m)

sol = Solution()
print(sol.findMaxForm(["10", "0001", "111001", "1", "0"], m = 5, n = 3))