# https://leetcode.cn/problems/binary-string-with-substrings-representing-1-to-n/

class Solution:
    def queryString(self, s: str, n: int) -> bool:
        for num in range(1, n+1):
            binary = bin(num)[2:]
            if binary not in s:
                return False
            
        return True
    
sol = Solution()
print(sol.queryString("0110", 4))