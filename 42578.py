def solution(clothes):
    clothes_map = {}

    for c in clothes:
        if c[1] not in clothes_map:
            clothes_map[c[1]] = [c[0]]
        elif c[0] not in clothes_map[c[1]]:
            clothes_map[c[1]].append(c[0])

    sum = 1
    for key in clothes_map:
        sum *= len(clothes_map[key]) + 1

    return sum - 1

if __name__ == "__main__":
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
