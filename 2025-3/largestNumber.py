# https://leetcode.cn/problems/form-largest-integer-with-digits-that-add-up-to-target/
from functools import cache
from typing import List


            
def bigger(s1: str, s2: str) -> int:
    if s1 == "0" or s1 == "":
        return s2
    if s2 == "0" or s2 == "":
        return s1
    
    if len(s1) > len(s2):
        return s1
    elif len(s1) < len(s2):
        return s2
    
    for c1, c2 in zip(s1, s2):
        if c1 > c2:
            return s1
        elif c1 < c2:
            return s2
    
    return c1

def addnumer(c: str, n: int)->str:
    if c == "0":
        return "0"
    if c =="":
        return str(n)
    sn = str(n)
    length = len(c)

    for i in range(length):
        if c[i] < sn:
            return c[:i] + sn + c[i:]
    return  c + sn

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        n = len(cost)
        @cache
        def dfs(i, s):
            if i == n:
                return "" if s == 0 else "0"
            if s < cost[i]:
                return dfs(i+1, s)
            l = dfs(i+1, s)
            r = addnumer(dfs(i, s-cost[i]), i+1)
            return bigger(l, r)
        return dfs(0, target)

# print(addnumer("0", 1))
# print(addnumer("", 1))
# print(addnumer("321", 1))


sol=Solution()
print(sol.largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9))