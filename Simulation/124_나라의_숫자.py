def solution(n):
    answer = []
    arr = ["1", "2", "4"]
    i = 1

    n -= 1
    mul = 1
    while n >= 0:
        mul *= 3
        a = n % mul
        b = int(a // (mul / 3))

        answer.append(arr[b])

        n -= mul
        i += 1

    return ''.join(reversed(answer))


print(solution(27))