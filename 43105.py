rows = 0
dp = []


def dfs(index, row, triangle):
    if row == rows:
        return triangle[row][index]

    if not dp[row][index] == -1:
        return dp[row][index]

    dp[row][index] = triangle[row][index]
    dp[row][index] += max(dfs(index, row + 1, triangle), dfs(index + 1, row + 1, triangle))

    return dp[row][index]


def solution(triangle):
    global rows, dp
    rows = len(triangle) - 1

    dp = [[-1 for _ in t] for t in triangle]

    return dfs(0, 0, triangle)


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
