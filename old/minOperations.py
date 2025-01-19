# https://leetcode.cn/problems/equal-sum-arrays-with-minimum-number-of-operations/
# 执行用时：
# 156 ms
# , 在所有 Python3 提交中击败了
# 41.23%
# 的用户
# 内存消耗：
# 20.4 MB
# , 在所有 Python3 提交中击败了
# 66.67%
# 的用户

from collections import Counter

def minOperations(nums1, nums2) -> int:
    sum1, sum2 = sum(nums1), sum(nums2)
    if len(nums1) > len(nums2) * 6 or len(nums2) > len(nums1) * 6:
        return -1

    if sum1 == sum2:
        return 0
    
    small, big = (nums1, nums2) if sum1 < sum2 else (nums2, nums1)
    diff = abs(sum1 - sum2)
    c_small = Counter(small)
    c_big = Counter(big)
    ret = 0
    for i in range(1, 7):
        temp = 0
        for c1 in range(c_small[i] + c_big[7-i]):
            temp +=1
            if temp * (6-i) >= diff:
                return temp + ret
            
        diff -= (6 - i) * temp
        ret += temp

    return -1

print(minOperations([5,2,1,5,2,2,2,2,4,3,3,5], [1,4,5,5,6,3,1,3,3]))