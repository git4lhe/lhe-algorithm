from itertools import combinations


def solution(nums):
    answer = 0
    nums.sort()

    value = sum(nums[-3:])
    d = [1] * (value + 1)
    d[0] = 0

    for i in range(2, value + 1):
        for j in range(2 * i, value + 1, i):
            d[j] = 0

    for i in combinations(nums, 3):
        n = sum(i)
        answer += d[n]

    return answer