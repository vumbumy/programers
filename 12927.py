import heapq


def solution(n, works):
    if sum(works) <= n:
        return 0

    heap = []
    for w in works:
        heapq.heappush(heap, -w)

    # print(heap)

    while n > 0:
        w = heapq.heappop(heap)
        w += 1
        n -= 1

        heapq.heappush(heap, w)

    # print(heap)

    return sum([w * w for w in heap])


print(solution(4, [4, 3, 3]))
print(solution(1, [2, 1, 2]))
print(solution(1, [5, 1, 2]))
print(solution(2, [5, 1, 2]))
print(solution(1, [2, 1, 2]))
print(solution(3, [1, 1]))
