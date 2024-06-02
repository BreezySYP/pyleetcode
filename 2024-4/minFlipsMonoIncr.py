## https://leetcode.cn/problems/flip-string-to-monotone-increasing/


# class Solution:
#     def minFlipsMonoIncr(self, s: str) -> int:
#         start = 0
#         end = len(s) - 1
#         for i in range(len(s)):
#             if s[i] == '1':
#                 start = i
#                 break

#         if s[start] == 0:
#             return 0
        
        
#         curr = start

#         while curr + 1 <= end:


#         if end == start:
#             return 0
        
#         subs = s[start:end+1]
#         count1 = subs.count('1')
#         count0 = subs.count('0')
#         return count1 if count0 > count1 else  count0

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        ans = count = 0
        for c in s:
            if c == '1':
                count += 1
            elif c =='0' and count > 0:
                count -= 1
                ans += 1
        return ans 


sol = Solution()
print(sol.minFlipsMonoIncr("10011111110010111011"))


