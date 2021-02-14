def lcm(a, b):
    a, b = min(a, b), max(a, b)

    while (1):
        if b == 0:
            break
        a, b = b, a % b

    return a


def solution(arr):
    answer = 1
    for i in arr:
        answer = answer * i // lcm(answer, i)
        print(answer)

    return answer


print(solution([2, 6, 8, 14]))