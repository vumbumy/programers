def find_w_in_line(card, word):
    visited = [False] * 3

    for c in word:
        found = False

        for i in range(3):
            if c in card[i]:
                visited[i] = True
                found = True
                card[i] = card[i].replace(c, '', 1)

        if not found:
            return False

    return all(visited)


def solution(card, word):
    answer = []

    for w in word:
        if find_w_in_line(card[:], w):
            answer.append(w)

    return answer if len(answer) > 0 else ["-1"]

print(
    solution(
        ["ABACDEFG", "NOPQRSTU", "HIJKLKMM"],
        ["GPQM", "GPMZ", "EFU", "MMNA"]
    )
)
