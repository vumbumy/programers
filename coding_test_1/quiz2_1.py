len_sticker = 0
dp = []


def dfs(i, sticker):
    dp = [-1] * len_sticker

    stack = [(i, sticker[i], len_sticker, sticker[:])]

    max_sum = 0
    while len(stack) != 0:
        index, sum, remain, stk = stack.pop()
        # print(index, sum, stk, dp)
        # input()

        max_sum = max(max_sum, sum)
        if remain == 0:
            continue

        if sum <= dp[index]:
            continue

        dp[index] = sum

        befr_index = index - 1
        next_index = (index + 1) % len_sticker

        befr = stk[befr_index]
        this = stk[index]
        next = stk[next_index]

        if befr == -1:
            remain -=1
        if next == -1:
            remain -=1

        stk[befr_index] = -1
        stk[index] = -1
        stk[next_index] = -1

        next2_index = (index + 2) % len_sticker
        if stk[next2_index] != -1:
            stack.append((next2_index, sum + stk[next2_index], remain - 1, stk[:]))

        next3_index = (index + 3) % len_sticker
        if stk[next3_index] != -1:
            stack.append((next3_index, sum + stk[next3_index], remain - 1, stk[:]))

    return max_sum


def solution(sticker):
    global len_sticker, dp

    len_sticker = len(sticker)
    if len_sticker == 1:
        return sticker[0]

    a = dfs(0, sticker)
    b = dfs(1, sticker)

    return max(a, b)


import random


print(solution([1]))
print(solution([2, 3]))
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
print(solution([1, 3, 2, 5, 4]))
print(solution([random.randint(1, 100) for _ in range(500)]))