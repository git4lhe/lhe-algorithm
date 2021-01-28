import math


def solution(n):
    answer = math.sqrt(n)

    if int(answer) * int(answer) == n:
        return (answer + 1) ** 2

    return -1