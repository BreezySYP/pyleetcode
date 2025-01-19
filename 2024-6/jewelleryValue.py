# https://leetcode.cn/problems/li-wu-de-zui-da-jie-zhi-lcof/
from typing import List


class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
        X = len(frame)
        Y = len(frame[0])
        dp = [[0 for i in range(Y)] for j in range(X)]
        for i in range(X):
            for j in range(Y):
                x = dp[i][j-1] if j > 0 else 0
                y = dp[i-1][j] if i > 0 else 0
                dp[i][j] = max(x + frame[i][j], y + frame[i][j])

        return max([max(n) for n in dp])

