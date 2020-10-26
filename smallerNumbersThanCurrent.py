#https://leetcode-cn.com/problems/how-many-numbers-are-smaller-than-the-current-number/
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        bucket = [0] * 101

        for i in nums:
            bucket[i]+=1

        return [sum(bucket[:i]) for i in nums]

sol = Solution()
print(sol.smallerNumbersThanCurrent([8,1,2,2,3]))