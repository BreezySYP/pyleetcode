# https://leetcode.cn/problems/maximize-sum-of-array-after-k-negations/
import heapq

def largestSumAfterKNegations(nums, k) -> int:

    minus_queue = []
    plus_queue = []
    for i in range(len(nums)):
        if nums[i] < 0:
            minus_queue.append(abs(nums[i]))
        else:
            plus_queue.append(nums[i])

    if k <= len(minus_queue):
        top_k = heapq.nlargest(k, minus_queue)
        return sum(nums) + 2 * sum(top_k)
    else:
        min_plus = 0 if (k - len(minus_queue)) % 2 == 0 else min(plus_queue + minus_queue)
        return sum(nums) + 2 * sum(minus_queue) - 2 * min_plus


print(largestSumAfterKNegations([-8,3,-5,-3,-5,-2], 6))