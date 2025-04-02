from functools import cache
from typing import List

class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        # 矩阵行数和列数
        m = len(mat)
        n = len(mat[0])

        # 对每一行去重并排序，减少不必要的计算
        mat = [sorted(set(row)) for row in mat]

        # 定义递归函数，带缓存
        @cache
        def dfs(row: int, current_sum: int) -> int:
            # 如果已经处理完所有行，返回当前和与目标的绝对差
            if row == m:
                return abs(current_sum - target)
            
            # 初始化最小绝对差
            min_diff = float('inf')

            # 遍历当前行的所有元素，尝试选择每个元素
            for num in mat[row]:
                # 递归计算下一行的最小绝对差
                min_diff = min(min_diff, dfs(row + 1, current_sum + num))
                
                # 如果当前和已经大于目标值，后续只会更大，可以提前剪枝
                if current_sum + num > target:
                    break

            return min_diff

        # 从第 0 行开始，当前和为 0
        return dfs(0, 0)

# 示例用法
sol = Solution()
mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
target = 13
print(sol.minimizeTheDifference(mat, target))  # 输出: 0