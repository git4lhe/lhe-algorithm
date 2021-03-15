def solution(n, times):
    answer = 0

    max_value = max(times) * n
    left = 1
    right = max_value + 1
    # max_value + 1 인 경우는, 최악의 경우

    while left <= right:
        mid = (left + right) // 2

        cnt = 0
        for time in times:
            cnt += mid // time
            if cnt >= n : break # 꼭 등호도 포함

        if cnt >= n:
            answer = mid
            right = mid - 1

        else:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
