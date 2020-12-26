dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -1


def dfs(i, j, k, count, board):
    global answer
    # for row in board:
    #     print(row)
    # print(i, j, k, count)
    # input()

    for d in range(4):
        y = i + dy[d]
        x = j + dx[d]

        if 0 <= y < 4 and 0 <= x < 4 and board[y][x] != -1 and k == board[y][x]:
            board[i][j] = -1
            dfs(y, x, k, count + 1, board)
            board[i][j] = k

    answer = max(answer, count)


def solution(board):
    global answer

    answer = -1

    for i in range(4):
        for j in range(4):
            if board[i][j] != -1:
                k = board[i][j]

                board[i][j] = -1
                dfs(i, j, k, 1, board)
                board[i][j] = k

    return answer if answer != 1 else -1


print(solution([[3,2,3,2], [2,1,1,2], [1,1,2,1], [4,1,1,1]]))
print(solution([[4,2,3,2], [2,1,2,4], [1,2,3,1], [4,1,4,3]]	))