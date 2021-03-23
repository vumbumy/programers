import queue

n, m = 0, 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

MAX_COST = (100 + 100) * 100 + 1


def find_robot(board):
    global n, m

    for y in range(n):
        for x in range(m):
            if 2 == board[y][x]:
                return x, y


def is_range(x, y):
    global n, m

    return 0 <= x < m and 0 <= y < n


def solution(board, c):
    global n, m

    n = len(board)
    m = len(board[0])

    answer = MAX_COST

    robot = find_robot(board)

    q = queue.Queue()

    q.put((robot[0], robot[1], 0))

    dp = []
    for i in range(n):
        dp.append([MAX_COST] * m)

    while not q.empty():
        x, y, cost = q.get()

        if board[y][x] == 3:
            answer = min(answer, cost)

        if dp[y][x] <= cost or answer <= cost:
            continue

        dp[y][x] = cost

        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if is_range(xx, yy):
                q.put((xx, yy, cost + 1 + (c if board[yy][xx] == 1 else 0)))

    return answer

print(
    solution(
        [
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3],
            [0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
        ],
        2
    )
)
print(
    solution(
        [
            [3, 0, 0],
            [0, 0, 2],
        ],
        10
    )
)
