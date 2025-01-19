from typing import List


MOD = 10**9+7
class Solution:
    def pathsWithMaxScore(self, board: List[str]) -> List[int]:
        m = len(board)
        n = len(board[0])

        ret = [[[0,0] for _ in range(n) ] for _ in range(m)]
        ret[-1][-1] = [0,1]

        for i in range(m-2, -1, -1):
            pre = ret[i+1][-1]
            val =  board[i][-1] if board[i][-1] != 'E' else 0
            if (pre[0] == -1 and pre[1] == -1) or val == 'X':
                ret[i][-1] = [-1,-1]
                continue
            ret[i][-1][0] = int(val) + pre[0]
            ret[i][-1][1] = 1 

        for i in range(n-2, -1 , -1):
            pre = ret[-1][i+1]
            val = board[-1][i] if board[-1][i] != 'E' else 0
            if (pre[0] == -1 and pre[1] == -1) or val == 'X':
                ret[-1][i] = [-1,-1]
                continue
            ret[-1][i][0] = int(val) + pre[0]
            ret[-1][i][1] = 1
        # print(ret)

        for i in range(m-2, -1, -1):
            for j in range(n-2, -1, -1):
                val = board[i][j] if board[i][j] != 'E' else 0
                bot = ret[i+1][j]
                right = ret[i][j+1]
                bot_right = ret[i+1][j+1]
                max_val = max(bot[0] , right[0] , bot_right[0])
                if max_val == -1 or val == 'X':
                    ret[i][j] = [-1,-1]
                    continue
                ret[i][j][0] = max_val + int(val)
                ret[i][j][1] = (bot[1] if max_val == bot[0] else 0 ) + (right[1] if max_val == right[0] else 0) + (bot_right[1] if max_val == bot_right[0] else 0)

        # print(ret)
        return [ret[0][0][0] % MOD, ret[0][0][1]% MOD] if ret[0][0][0] != -1 else [0, 0]
    

sol = Solution()
# sol.pathsWithMaxScore(["E23",
#                        "2X2",
#                        "12S"])

sol.pathsWithMaxScore(["EX","XS"])
        

