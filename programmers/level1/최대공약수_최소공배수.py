# 유클리드 호제법
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def solution(n, m):
    answer = []
    a, b = min(n, m), max(n, m)

    answer.append(gcd(a, b))
    answer.append(n * m / gcd(a, b))

    return answer