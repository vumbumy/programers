def split(n):
    nums = []

    while n > 0:
        num = n % 10
        if num > 0:
            nums.append(num)

        n = int(n / 10)

    return set(nums)


def solution(n):
    answer = 0

    nums = split(n)

    for num in nums:
        if n % num ==0:
            answer += 1

    return answer


print(solution(2232))
