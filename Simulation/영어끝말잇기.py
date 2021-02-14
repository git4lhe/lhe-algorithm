from collections import defaultdict


def solution(n, words):
    answer = []

    prev = defaultdict(lambda: 0)
    prev[words[0]] = 1

    for i in range(1, len(words)):
        if words[i - 1][-1] == words[i][0]:
            # FIRST 단어
            if not prev[words[i]]:
                prev[words[i]] = 1
            # 중복
            else:
                print(i, words[i])
                return [i % n + 1, (i + n) // n]
        else:
            return [i % n + 1, (i + n) // n]

    return [0, 0]