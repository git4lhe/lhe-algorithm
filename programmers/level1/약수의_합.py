def solution(n):
    if n == 0 or n == 1:
        return n

    arr = [0] * (n + 1)
    arr[1] = 1

    for i in range(1, n + 1):
        if arr[i] == 0:
            if n % i == 0:
                arr[i] = i
                arr[n // i] = n // i

    return sum(arr)