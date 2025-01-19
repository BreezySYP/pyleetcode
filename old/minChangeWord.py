def minChangeWord(word1, word2):
    if word1 == None or word2 == None:
        return

    len1 = len(word1) + 1
    len2 = len(word2) + 1

    if len1 == 0:
        return len2
    if len2 == 0:
        return len1
    
    dp = [[0 for col in range(len1)] for row in range(len2)]

    for i in range(1, len1):
        dp[0][i] = dp[0][i-1] + 1

    for i in range(1, len2):
        dp[i][0] = dp[i-1][0] + 1

    for i in range(1, len2):
        for j in range(1, len1):
            if word1[j-1] == word2[i-1]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])+1
    
    return dp[len2-1][len1 - 1]

print(minChangeWord("ros", "horse"))