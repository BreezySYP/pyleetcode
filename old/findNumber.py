#https://leetcode-cn.com/problems/find-numbers-with-even-number-of-digits/

class Solution:
    def findNumbers(self, nums) -> int:
        return sum(1 for num in nums if len(str(num)) % 2 == 0)