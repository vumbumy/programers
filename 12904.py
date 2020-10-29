def solution(s):
    len_s = len(s)
    if len_s == 1:
        return 1

    for l in range(len_s, 1, -1):
        for i in range(len_s - l + 1):
            # print(i, i + l)
            this = s[i:l + i]
            # print(this)
            if this == this[::-1]:
                return l

    return 0


assert solution("") is 0
assert solution("a") is 1
assert solution("d") is 1
assert solution("abcdcba") is 7
assert solution("abcbaqwertrewqq") is 9
assert solution("abcbaqwqabcba") is 13

print("DONE")
