def merge(s1, s2, min_len):
    for i in range(min_len):
        b = s1[len(s1) - min_len + i:]
        f = s2[:min_len - i]
        if b == f:
            return s1[:len(s1) - min_len + i] + b + s2[min_len - i:]

    return s1 + s2


def solution(s1, s2):
    min_len = min(len(s1), len(s2))

    merge1 = merge(s1, s2, min_len)
    merge2 = merge(s2, s1, min_len)

    if len(merge1) < len(merge2):
        return merge1
    elif len(merge1) > len(merge2):
        return merge2

    return sorted([merge1, merge2], key=lambda x: (x.casefold(), x.swapcase()))[0]

print(solution("xyZA","ABCxy"))
print(solution("AxA","AyA"))
print(solution("aA","Aa"))
print(solution("aaaA","Aaaa"))
print(solution("abc","bcab"))
print(solution("abc","ddd"))