import sys
if __name__ == "__main__":
    n = int(sys.stdin.readline().strip())

    if n > 7 or n < 3:
        print(-1)
        exit()
    m = int(sys.stdin.readline().strip())

    num = pow(10, n - 1)
    flowers = []
    for i in range(num, num * 10 - 1):
        tempflower = 0
        tempBit = i
        for j in range(n):
            tempflower += pow(tempBit % 10, n)
            tempBit = int(tempBit / 10)

        if tempflower == i:
            flowers.append(i)

    if len(flowers) > m:
        print(flowers[m])
    else:
        print(m * flowers[len(flowers) - 1])