#https://leetcode.cn/problems/interleaving-string/
from functools import cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False

        
        @cache
        def dfs(i, j, k):
            if j < 0 and i < 0:
                return k < 0 
            if j < 0:
                return s1[:i+1] == s3[:k+1]
            if i < 0:
                return s2[:j+1] == s3[:k+1]
            
            if s1[i] == s3[k] and s2[j] == s3[k]:
                return dfs(i-1, j, k-1) or dfs(i,j-1,k-1)
            elif s1[i] == s3[k]:
                return dfs(i-1, j, k-1)
            elif s2[j] == s3[k] :
                return dfs(i, j-1, k-1)
            return False
        return dfs(len1-1, len2-1, len3-1)
     
            
    
sol = Solution()
print(sol.isInterleave("c", "", "a"))
print(sol.isInterleave("a", "", "a"))
print(sol.isInterleave("abc", "aa", "aaabc"))