import queue


def solution(n, k):
    q = queue.Queue()

    count = 0

    q.put((0, []))

    answer = []
    while not q.empty():
        index, arr = q.get()

        if n == len(arr):
            count += 1
            if count == k:
                answer = arr
                break
            continue

        for i in range(n):
            if i not in arr:
                arr.append(i)

                q.put((i + 1, arr[:]))

                arr.pop()

    return [i + 1 for i in answer]


print(solution(3, 5))
print(solution(20, 100))
