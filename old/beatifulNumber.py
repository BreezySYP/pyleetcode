def nextBeautifulNumber(n):
    ln = len(str(n))

    l6 = [122333, 155555, 212333,221333,223133,223313, 223331, 132233, 132323, 132332, 123233, 123323, 123333, 224444, 242444, 244244, 244424, 244442, 422444, 424244, 424424, 424442, 442244, 442424, 442442, 444224, 444242, 444422, 515555, 551555, 555155, 555515, 555551, 666666]
    l5 = [14444, 22333, 23233, 23323, 23332, 32233, 32323, 32332, 33223, 33232, 33322, 41444, 44144, 44414, 44441, 55555]
    l4 = [1333, 3133, 3313 ,3331, 4444]
    l3 = [122, 212, 221, 333]
    l2 = [22]
    l1 = [1]
    l = [l1, l2 ,l3 ,l4 ,l5, l6]
    
    if n < l[ln-1][-1]:
        for i in l[ln-1]:
            if n < i:
                return i
    else:
        return l[ln][0]

# def buildNum(num_list):
#     ret = []
#     ln = len(num_list)
#     for row1 in range(ln):
#         for row2 in range(row1+1, ln):
#             for i in range(len(num_list[row1])):
#                 for j in range(len(num_list[row2])):
#                     temp = num_list.copy()
#                     print(temp)
#                     temp_val = temp[row1][i]
#                     temp[row1][i] = temp[row2][j]
#                     temp[row2][j] = temp_val
#                     print(row1, row2, i, j, temp)
#                     ret.append(int("".join([str(m) for n in temp for m in n])))

#     return ret

print(buildNum([[1], [2,2],[3,3,3]]))
122333
# print(nextBeautifulNumber(44325))

        
    