0#https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/
def maxProfit(prices):
    dp = [0 for _ in prices]

    for i in range(1, len(prices)):
        dp[i] = dp[i-1]
        if prices[i] > prices[i-1]:
            dp[i] += prices[i] - prices[i-1]

    return dp[-1]

#print(maxProfit([1,2,3,4,5]))
print(maxProfit([5,2,7,4,8]))
        