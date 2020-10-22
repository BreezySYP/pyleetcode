
shapes = (5,6)
cord = [[2,2,3] for i in shapes]

print(cord)

result = [[0 for col in range(5)] for row in range(6)]

result[cord] = 1


print(result)