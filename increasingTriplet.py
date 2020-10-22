#https://leetcode-cn.com/problems/increasing-triplet-subsequence/
import sys

def lengthOfLST(nums):
    if not nums:
        return 0
    
    first = sys.maxsize
    second = sys.maxsize

    for num in nums:
        if first >= num:
            first = num
        elif second >= num:
            second = num
        else:
            return True
    return False

print(lengthOfLST([2,1,2]))