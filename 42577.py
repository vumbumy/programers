def solution(phone_book):
    phone_book.sort(key=len)

    prefixMap = {}

    for phone in phone_book:
        word = ""
        for p in phone:
            word += p

            if word in prefixMap:
                return False
        prefixMap[word] = True

    return True


if __name__ == "__main__":
    print(solution(["119", "97674223", "1195524421", "11"]))
