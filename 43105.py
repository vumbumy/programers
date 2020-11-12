import queue


def solution(triangle):
    rows = len(triangle) - 1

    answer = 0

    q = queue.Queue()
    q.put((0, 0, 0))

    while not q.empty():
        index, row, sum = q.get()

        sum += triangle[row][index]

        if row == rows:
            answer = max(answer, sum)
            continue

        q.put((index, row + 1, sum))
        q.put((index + 1, row + 1, sum))

    return answer


print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
