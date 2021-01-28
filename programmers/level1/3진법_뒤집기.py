def solution(n):
    answer = ''

    # using logic 3진법
    while n >= 1:
        rest = n % 3
        n = n // 3
        answer += str(rest)

    res = 0
    for i, n in enumerate(reversed(answer)):
        res += int(n) * 3 ** i

    return res