##https://leetcode.cn/problems/non-negative-integers-without-consecutive-ones/description/

class Solution:
    def findIntegers(self, n: int) -> int:
        binNum = bin(n)
        l = len(binNum)
        count = 0
        for i in range(l):
            binNum[i] == '1'
            count += self.findAdjaction(l - 1 - i)

        return n - count



    def findAdjaction(self, n : int) -> int:
        if n == 1:
            return 0
        return (pow(2, n) - pow(2, n - 1))/2 + self.findAdjaction(self, n - 2)