#https://leetcode-cn.com/problems/number-of-boomerangs/

class Solution:
    def numberOfBoomerangs(self, points) -> int:
        count = 0
        dict = {}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]

                distance = pow(p1[0] - p2[0], 2) + pow(p1[1] - p2[1], 2)
                if distance in dict.keys():
                    if p1 in dict[distance] :
                        count += 2
                    if p2 in dict[distance]:
                        count += 2

                    dict[distance].append(p1)
                    dict[distance].append(p2)
                else:
                    dict[distance] = [p1, p2]

        return count
                

sol = Solution()
print(sol.numberOfBoomerangs([[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
