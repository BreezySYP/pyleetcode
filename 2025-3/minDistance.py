# https://leetcode.cn/problems/delete-operation-for-two-strings/
from functools import cache


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        @cache
        def dfs(i, j):
            if i < 0:
                return j+1
            if j < 0:
                return i+1
            if word1[i] == word2[j]:
                return dfs(i-1, j-1)
            return min(dfs(i-1, j), dfs(i, j-1))+1
        return dfs(n-1, m-1)