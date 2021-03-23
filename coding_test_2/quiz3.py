def solution(n):
    for i in range(int(n / 5), 0, -1):
        temp_n = n % (i * 5)

        if temp_n % 3 == 0:
            return i + int(temp_n/3)

    if n % 3 == 0:
        return int(n/3)

    return -1




print(solution(15))
print(solution(7))
print(solution(1000))
print(solution(3))
print(solution(5))
print(solution(8))
print(solution(12))
print(solution(15))
print(solution(13))
print(solution(17))