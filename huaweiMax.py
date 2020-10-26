def getDescDict(num):
    desc = [0] * 10 
    while num > 0:
        desc[num % 10] += 1
        num = int(num / 10)
    return desc

def max(a, b):
    num1 = getDescDict(a)
    num2 = getDescDict(b)

    sumCount = [num1[i] + num2[i] for i in range(0, 10)]
    
    result = ''
    for i in range(9, -1, -1):
        if sumCount[i] > 0:
            numStr = ''
            for j in range(sumCount[i]):
                numStr += str(i) 
            result+= numStr

    return result

print(max(91324324, 10123231))



