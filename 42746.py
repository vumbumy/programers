def num_to_arr(n):
    arr = []

    while n > 0:
        arr.append(n % 10)
        n = int(n/10)

    arr.reverse()

    return arr if len(arr) != 0 else [0]


def find_bigger(a, b):
    len_a = len(a)
    len_b = len(b)

    index_a = 0
    index_b = 0

    while True:
        if a[index_a] != b[index_b]:
            return 1 if a[index_a] > b[index_b] else -1

        if index_a == len_a - 1 and index_b == len_b - 1:
            break

        if index_a < len_a - 1:
            index_a += 1

        if index_b < len_b - 1:
            index_b += 1

    return 0 if len_a == len_b else (1 if len_a < len_b else -1)


def solution(numbers):
    answer = ''

    len_a = len(numbers)

    for i in range(len_a):

        len_b = len_a - i
        # print(len_b, ":", end="")
        for j in range(i, len_a):
            a = num_to_arr(numbers[i])
            b = num_to_arr(numbers[j])

            if find_bigger(a, b) == -1:
                temp = numbers[j]
                numbers[j] = numbers[i]
                numbers[i] = temp

            # print(numbers)

        # for n in numbers:
        if len(answer) == 0 and numbers[i] == 0:
            continue

        answer += str(numbers[i])

    return answer if len(answer) != 0 else '0'
