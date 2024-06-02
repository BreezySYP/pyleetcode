# https://leetcode.cn/problems/WhsWhI/

# refs:
# https://leetcode.cn/problems/friend-circles/solutions/58682/union-find-suan-fa-xiang-jie-by-labuladong/
# https://zhuanlan.zhihu.com/p/93647900

def longestConsecutive(nums) -> int:
    if not nums:
        return 0

    exist = set(nums)
    
    longest = 0
    for num in nums:
        if num - 1 not in exist:

            current = num
            temp = 1

            while current + 1 in exist:
                current += 1
                temp += 1

                longest = max(longest, temp)
    return longest

print(longestConsecutive([100,4,200,1,3,2]))