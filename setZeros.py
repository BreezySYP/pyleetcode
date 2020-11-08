#https://leetcode-cn.com/problems/zero-matrix-lcci/
# Improve: In-place make first element zero if list contains zero,
def setZeros(matrix):
    zeroRowIndex = []
    zeroColIndex = []

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[i])):
            if matrix[i][j] == 0:
                zeroRowIndex.append(i)
                zeroColIndex.append(j)

    for r in zeroRowIndex:
        matrix[r] = [0 for _ in range(len(matrix[0]))]
        
    for c in zeroColIndex:
        for l in range(0, len(matrix)):
             matrix[l][c] = 0

martix = [
    [0,1,2,0], 
    [3,4,5,2], 
    [1,3,1,5]
]
setZeros(martix)
print(martix) 