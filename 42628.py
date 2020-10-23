def solution(operations):
    answer = []

    for op in operations:
        cmd, val = op.split()

        if cmd == 'I':
            answer.append(int(val))
        elif cmd == 'D' and len(answer) != 0:
            if val == '1':
                answer.remove(max(answer))
            else:
                answer.remove(min(answer))

    if len(answer) == 0:
        answer = [0]

    return [max(answer), min(answer)]


print(solution(["I 16", "D 1"]))
print(solution(["I 7", "I 5", "I -5", "D -1"]))
