def recursive(n, answer):
    if n == 0:
        return
    answer.append(n % 10)
    return recursive(n // 10, answer)


def solution(n):
    answer = []
    recursive(n, answer)

    return answer