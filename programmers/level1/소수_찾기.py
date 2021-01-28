def solution(n):
    a = [0] * (n + 1)

    for i in range(1, n + 1):
        a[i] = i

    for i in range(2, n + 1):
        if a[i] == 0:
            continue
        for j in range(2 * i, n + 1, i):
            a[j] = 0

    return n - a.count(0)