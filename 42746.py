def solution(numbers):
    str_nums = [str(n) for n in numbers]
    max_len = max([len(n) for n in str_nums])

    new_nums = []
    for s in str_nums:
        len_s = len(s)
        key = s
        for i in range(max_len - len_s):
            key += str(int(s[i % len_s]))
        new_nums.append([key, s])

    nums = sorted(new_nums, reverse=True, key=lambda x: x[0])

    answer = ""
    for n in nums:
        answer += n[1]

    return str(int(answer))


print(solution([12, 1213]))
print(solution([12, 1212]))
print(solution([12, 121]))
print(solution([12, 122]))
