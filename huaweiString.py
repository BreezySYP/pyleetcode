import sys
def UpperOrLowerSubString(s, k):
    strs = s.split('-')
    new = strs[0] + '-'

    remain = ''
    for i in range(1, len(strs)):
        remain += strs[i]

    subs = []
    for i in range(0, len(remain), k):
        subs.append(remain[i:i+k])

    for sub in subs:
        smallcase = 0
        bigcase = 0
        for j in range(len(sub)):
            if sub[j] >= 'a' and sub[j] <= 'z':
                smallcase += 1
            elif sub[j] >= 'A' and sub[j] <= 'Z':
                bigcase += 1

        if smallcase > bigcase:
            new += sub.lower()
        elif smallcase < bigcase:
            new += sub.upper()
        else:
            new += sub

        new += '-'
    return new[:len(new)-1]

if __name__ == "__main__":
    
    k = int(sys.stdin.readline().strip())
    s = sys.stdin.readline().strip()
    print(UpperOrLowerSubString(s, k))