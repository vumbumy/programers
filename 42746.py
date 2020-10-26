def solution(numbers):
    print(numbers, end=" -> ")
    str_nums = [str(n) for n in numbers]
    max_len = max([len(n) for n in str_nums])

    new_nums = []
    for s in str_nums:
        len_s = len(s)
        key = s + (max_len - len_s) * str(int(s[len_s-1]))
        new_nums.append([key, -len_s, s])

    # print(new_nums)

    # nums = []
    nums = sorted(new_nums, reverse=True, key=lambda x: (x[0], x[1]))
    # print(nums)

    answer = ""
    for n in nums:
        answer += n[2]

    return str(int(answer))


print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([3, 30, 32, 5, 9]))
print(solution([7, 0, 0, 0]))
print(solution([0, 0]))
print(solution([40,403 ]))
print(solution([40,405]))
print(solution([40,404]))
print(solution([12,121]))
print(solution([2,22,223]))
print(solution([21,212]))
print(solution([41,415]))
print(solution([2,22 ]))
print(solution([70,0,0,0]))
print(solution([0,0,0,0]))
print(solution([0,0,0,1000]))
print(solution([12,1213]))
print(solution([21, 212, 211, 22]))
