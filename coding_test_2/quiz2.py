def solution(grade):
    ranks = [0] * (max(grade) + 1)

    this = 0
    rank = 1
    for g in sorted(grade, reverse=True):
        if this != g:
            this = g
            ranks[g] = rank

        rank +=1

    return [ranks[g] for g in grade]


print(solution([2, 2, 1]))
print(solution([3,2,1,2]))