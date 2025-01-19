# https://leetcode.cn/problems/cyclically-rotating-a-grid/
# 执行用时：
# 140 ms
# , 在所有 Python3 提交中击败了
# 62.50%
# 的用户
# 内存消耗：
# 16.5 MB
# , 在所有 Python3 提交中击败了
# 6.25%
# 的用户
# 通过测试用例：
# 68 / 68

import math


def rotate_grid(grid, k):
    m = len(grid)
    n = len(grid[0])
    layer = math.floor(min(m, n) / 2)

    for i in range(layer):
        # left top [i, i], left bottom [m - 1 - i, i], right top [i, n -1 - i], right bottom [m -1 - i, n - 1- i]
        temp = []
        for row in range(i, m - i):
            temp.append([grid[row][i], row, i])

        for col in range(i+1, n - i):
            temp.append([grid[m - i - 1][col], m-i-1, col])

        for row in range(m - i - 2, i, -1):
            temp.append([grid[row][n - 1 -i], row, n-1-i])

        for col in range(n - i - 1, i, -1):
            temp.append([grid[i][col], i, col])

        for temp_i in range(0,len(temp)):
            rotate_i = (len(temp) - (k % len(temp)) + temp_i) % len(temp)
            # print(rotate_i)
            grid_m = temp[temp_i][1]
            grid_n = temp[temp_i][2]
            grid[grid_m][grid_n] = temp[rotate_i][0]

    return grid


# rotate_grid([[1, 2, 3, 4], [5, 6, 7, 8], [
#             9, 10, 11, 12], [13, 14, 15, 16]], k=2)
rotate_grid([[40,10],[30,20]], k=2)
