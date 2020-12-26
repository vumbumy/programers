len_sticker = 0
dp = []


def dfs(index, sticker, remain):
    if remain == 0:
        return 0

    if dp[index] != -1:
        return dp[index]

    befr_index = index - 1
    next_index = (index + 1) % len_sticker

    befr = sticker[befr_index]
    dp[index] = sticker[index]
    next = sticker[next_index]

    remain -=1
    if befr == -1:
        remain -=1
    if next == -1:
        remain -=1

    max_sum = 0

    sticker[befr_index] = -1
    sticker[index] = -1
    sticker[next_index] = -1

    next2_index = (index + 2) % len_sticker
    if sticker[next2_index] != -1:
        max_sum = max(max_sum, dfs(next2_index, sticker, remain))

    next3_index = (index + 3) % len_sticker
    if sticker[next3_index] != -1:
        max_sum = max(max_sum, dfs(next3_index, sticker, remain))

    sticker[befr_index] = befr
    sticker[index] = dp[index]
    sticker[next_index] = next

    dp[index] += max_sum

    return dp[index]


def solution(sticker):
    import sys
    sys.setrecursionlimit(100000)

    global len_sticker, dp

    len_sticker = len(sticker)
    if len_sticker == 1:
        return sticker[0]

    dp = [-1] * len_sticker
    a = dfs(0, sticker, len_sticker)

    dp = [-1] * len_sticker
    b = dfs(1, sticker, len_sticker)

    # dp = [-1] * len_sticker
    c = dfs(-1, sticker, len_sticker)

    return max(a, b)


import sys
import random


sys.setrecursionlimit(100001)
print(sys.getrecursionlimit())
print(solution([1]))
print(solution([2, 3]))
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
print(solution([1, 0, 0]))
print(solution([0, 1, 0]))
print(solution([0, 0, 1]))
print(solution([random.randint(1, 100) for _ in range(9000)]))