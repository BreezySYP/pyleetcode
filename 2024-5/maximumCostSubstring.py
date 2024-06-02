# https://leetcode.cn/problems/find-the-substring-with-maximum-cost/
from functools import cache


class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals) -> int:
        c_dict = {}
        [c_dict.update({c: ord(c)-96})  for c in s]
        [c_dict.update({chars[i]: vals[i]}) for i in range(len(chars))]

        dp = [c_dict.get(s[0])]
        for i in range(1, len(s)):
            maxsum = max(dp[i-1],0)+c_dict.get(s[i])
            dp.append(maxsum)
        dp.append(0)
        return max(dp)

sol = Solution()
print(sol.maximumCostSubstring('adaa', 'd', [-1000]))