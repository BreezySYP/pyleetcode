# https://leetcode.cn/problems/reconstruct-original-digits-from-english/

from collections import Counter


def originalDigits(s):
    c = Counter(s)

    cnt = [0] * 10
    cnt[0] = c["z"]
    cnt[2] = c["w"]
    cnt[4] = c["u"]
    cnt[6] = c["x"]
    cnt[8] = c["g"]

    cnt[3] = c["h"] - cnt[8]
    cnt[7] = c["s"] - cnt[6]
    cnt[5] = c["v"] - cnt[7]
    
    cnt[1] = c["o"] - cnt[2] - cnt[4] - cnt[0]
    cnt[9] = c["i"] - cnt[5] - cnt[6] - cnt[8]

    return "".join(str(x) * cnt[x] for x in range(10))

print(originalDigits("zeroonetwothreefourfivesixseveneightnine"))
