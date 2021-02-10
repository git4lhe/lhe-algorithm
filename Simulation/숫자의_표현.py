def solution(n):
    answer = 0
    for i in range(1, n):
        for j in range(i + 1, n):
            sum_value = (abs((j - i + 1)) * (i + j)) // 2
            if sum_value == n:
                answer += 1

            elif sum_value > n:
                break

    return answer + 1


print(solution(15))