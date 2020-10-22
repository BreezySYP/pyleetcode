#https://leetcode-cn.com/problems/ones-and-zeroes/

def findMaxForm(strs, m, n):
    if m == 0 and n == 0:
        return 0
    
    dp = [[0 for _ in len(n + 1)] for _ in len(m + 1)]
    

