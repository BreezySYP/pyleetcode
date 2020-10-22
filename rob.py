#https://leetcode-cn.com/problems/house-robber/

def rob(nums):
    if len(nums) == 1:
        return nums[0]

    size = len(nums)
    dp = [0] * size
    dp[0] = nums[0]
    dp[1] = max(dp[0], nums[1])

    for i in range(2, size):
        dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
    return dp[size - 1]

print(rob([2,1,1,2]))


    