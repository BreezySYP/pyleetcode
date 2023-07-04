'''给定一个非负整数，你至多可以交换一次数字中的任意两位。返回你能得到的最大值。

示例 1 :

输入: 2736
输出: 7236
解释: 交换数字2和数字7。
示例 2 :

输入: 9973
输出: 9973
解释: 不需要交换。
注意:

给定数字的范围是 [0, 108]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-swap
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。'''

class Solution:
    def maximumSwap(self, num: int) -> int:
        numStr = str(num)

        indices = [ -1 for i in range(10)]
    
        for i in range(len(numStr)):
            numInByte = int(numStr[i])
            indices[numInByte] = i

        for i in range(len(numStr)):
            numInByte = int(numStr[i])
            for j in range(9, -1, -1):
                if indices[j] > i and numInByte < j:

                    temp = list(numStr)
                    temp[i], temp[indices[j]] = temp[indices[j]], temp[i]
                    return int("".join(temp))

        return num

sol = Solution()
print(sol.maximumSwap(98368))