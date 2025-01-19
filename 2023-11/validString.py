# https://leetcode.cn/problems/check-if-word-is-valid-after-substitutions/
class Solution:
    def isValid(self, s: str) -> bool:
        cur = ""
        pre = s
        while pre != "":
            cur = pre.replace("abc", "")
            if cur == pre:
                break
            pre = cur

        return pre == ''
    
    
sol = Solution()
print(sol.isValid("abccba"))