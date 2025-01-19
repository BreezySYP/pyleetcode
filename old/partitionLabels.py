#https://leetcode-cn.com/problems/partition-labels/
class Solution(object):
    def partitionLabels(self, S):
        letterIndexes = {}

        for i in range(0, len(S)):
            if S[i] in letterIndexes.keys():
                letterIndexes[S[i]].append(i)
            else:
                letterIndexes[S[i]] = [i]
        

        result = [self.getStartAndEnd(letterIndexes[S[0]])]
        for key in letterIndexes:
            newRange = self.getStartAndEnd(letterIndexes[key])
            if not self.anyIntersect(newRange, result):
                result.append(newRange)

        return [(item[1] - item[0] + 1) for item in result]


    def getStartAndEnd(self, indexes):
        return [indexes[0], indexes[len(indexes) - 1]]

    def anyIntersect(self, newR, rangeHistory):
        for i in range(0, len(rangeHistory)):
            if (rangeHistory[i][0] <= newR[0] and rangeHistory[i][1] >= newR[0]) or (rangeHistory[i][0] <= newR[1] and rangeHistory[i][1] >= newR[1]):
                rangeHistory[i][1] = max(rangeHistory[i][1], newR[1])
                rangeHistory[i][0] = min(rangeHistory[i][0], newR[0])
                return True
        return False   

#print(partitionLabels("ababcbacadefegdehijhklij"))
sol = Solution()
print(sol.partitionLabels("dccccbaabe"))