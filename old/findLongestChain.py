#https://leetcode-cn.com/problems/maximum-length-of-pair-chain/

def findLongestChain(pairs):
    if not pairs:
        return 0
    dp = []

    for i in range(len(pairs)):
        dp.append(1)
        for j in range(i):
            if pairs[i][0] > pairs[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
                
    return max(dp)

print(findLongestChain([[3,4],[2,3],[1,2]]))