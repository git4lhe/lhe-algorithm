def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x


def solution(w, h):
    r = gcd(w, h)
    a, b = w // r, h // r
    answer = w * h - (a + b - 1) * r

    return answer