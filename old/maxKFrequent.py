
#https://leetcode-cn.com/problems/top-k-frequent-words/solution/qian-kge-gao-pin-dan-ci-by-leetcode/

import collections
import heapq

def topKFrequent(words, k):
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]


print(topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 2)) 
