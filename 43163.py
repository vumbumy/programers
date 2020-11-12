import queue


def changeable(a, b):
    is_diff = False
    for i in range(len(a)):
        if a[i] != b[i]:
            if is_diff:
                return False

            is_diff = True

    return True


answer = 0
global_target = ""
len_words = 0


def dfs(source, words, count):
    global answer, global_target

    if answer <= count:
        return

    if source == global_target:
        answer = min(answer, count)
        return

    for i in range(len_words):
        w = words[i]
        if w is not None and changeable(source, w):
            # print(source, w)
            words[i] = None
            dfs(w, words, count + 1)
            words[i] = w


def solution(begin, target, words):
    global global_target, len_words, answer

    global_target = target
    len_words = len(words)
    answer = len_words + 1

    dfs(begin, words, 0)

    return answer if answer <= len_words else 0


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log"]))
