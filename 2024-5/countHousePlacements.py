# https://leetcode.cn/problems/count-number-of-ways-to-place-houses/

class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [[1,1]]
        for i in range(1,n):
            noPlace = dp[i-1][0] + dp[i-1][1]
            place = dp[i-1][0]
            dp.append([noPlace, place])
        return ((dp[n-1][0] + dp[n-1][1])**2)%(10**9+7)
