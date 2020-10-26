#https://leetcode-cn.com/problems/longest-mountain-in-array/
class Solution:
    def longestMountain(self, A) -> int:
        peeks = []
        for i in range(1, len(A) - 1):
            if A[i] > A[i - 1] and A[i] > A[i + 1]:
                peeks.append(i)

        if len(peeks) == 0:
            return 0

        lengths = []
        for i in peeks:
            left = self.leftlowest(A, i)
            right = self.rightlowest(A, i)
            lengths.append(right-left+1)

        return max(lengths)

    def leftlowest(self, A, index):
        while A[index] > A[index-1]:
            index-=1
            if index <= 0:
                return index
        return index

    def rightlowest(self, A, index):
        while A[index] > A[index+1]:
            index+=1
            if index >= len(A)-1:
                return index
        return index

sol = Solution()
print (sol.longestMountain([0,1,2,3,4,5,4,3,2,1,0]))

        
