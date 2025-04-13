# https://leetcode.cn/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/ 
from functools import cache
from typing import Counter, List


class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        charnum = len(words[0])
        MOD = 1_000_000_007
        
        charCount = [Counter() for _ in range(charnum)]
        for word in words:
            for j in range(charnum):
                charCount[j][word[j]] += 1
        @cache
        def dfs(i, j):
            if i < j:
                return 0
            if j < 0:
                return 1
            return dfs(i-1, j-1) * charCount[i][target[j]] % MOD + dfs(i-1, j) % MOD 
        return dfs(charnum-1, len(target)-1) % MOD 
    
sol = Solution()
print(sol.numWays(["abab","baba","abba","baab"], "abba"))
            
            