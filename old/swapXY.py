#https://leetcode-cn.com/problems/minimum-swaps-to-make-strings-equal/

def swapXY(s1, s2):
    if len(s1) != len(s2) or len(s1) < 1:
        return -1

    xyCount = 0
    yxCount = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if s1[i] == 'x':
                xyCount +=1
            else:
                yxCount +=1
           
    if (xyCount + yxCount) % 2 != 0:
        return -1
    
    if xyCount % 2 == 0:
        return (xyCount + yxCount) / 2
    else:
        return xyCount / 2 + yxCount / 2 + 2


print(swapXY('xy', 'yx'))