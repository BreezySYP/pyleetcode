#https://leetcode-cn.com/problems/longest-increasing-subsequence/
'''
首先考虑题目问什么，就把什么定义成状态。
题目问最长上升子序列的长度，其实可以把「子序列的长度」定义成状态，但是发现「状态转移」不好做；
把「子序列的长度」定义成状态，事实上也可以，只是目前这样定义状态，没有定义得很清晰，具体做法在下文「方法三」；
为了从一个较短的上升子序列得到一个较长的上升子序列，我们主要关心这个较短的上升子序列结尾的元素。由于要保证子序列的相对顺序，
在程序读到一个新的数的时候，如果比已经得到的子序列的最后一个数还大，那么就可以放在这个子序列的最后，形成一个更长的子序列；
由于一个子序列一定会以一个数结尾，于是将状态定义成：dp[i] 表示以 nums[i] 结尾的「上升子序列」的长度。
注意：这个定义中 nums[i] 必须被选取，且必须是这个子序列的最后一个元素。

以nums[i]结尾的最长上升子序列长度，优于，当字符串长度为i时，最长上升子序列的长度。
'''

def lengthOfLST(nums):
    if not nums:
        return 0
    dp = []
    for i in range(len(nums)):
        dp.append(1)
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

print(lengthOfLST([10,9,2,5,3,7,101]))