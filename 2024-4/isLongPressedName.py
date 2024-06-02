## https://leetcode.cn/problems/long-pressed-name/
class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        if len(typed) < len(name):
            return False

        nameArr = self.charArray( name)
        typedArr = self.charArray( typed)

        if len(typedArr) != len(nameArr):
            return False
        
        for i in range(len(nameArr)):
            if nameArr[i][0] != typedArr[i][0]:
                return False
            if len(nameArr[i]) > len(typedArr[i]):
                return False
            
        return True
            
    def charArray(self, s):

        result = []

        curr_char = s[0]
        curr_group = [curr_char]

        for c in s[1:]:
            if c == curr_char:
                curr_group.append(c)
            else :
                result.append(curr_group)
                curr_char = c
                curr_group = [curr_char]

        result.append(curr_group)
        return result
        
        
