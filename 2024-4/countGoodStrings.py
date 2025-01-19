# https://leetcode.cn/problems/count-ways-to-build-good-strings/
class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [0 for _ in range(high+1)]
        dp[0] = 1
        for i in range(1, high+1):
            a = i - zero if i - zero >= 0 else 0
            b = i - one if i - one >= 0 else 0
            dp[i] = a+b
        return sum([dp[i] for i in range(low, high+1)]) % (10**9+7)