from itertools import permutations

def solution(numbers):
    answer = 0

    tmp = [i for i in numbers]
    tmp.sort(reverse=True)
    max_value = int("".join(tmp))

    sosu = [1] * (max_value + 1)
    sosu[0] = 0
    sosu[1] = 0

    for i in range(2, max_value+1):
        if sosu[i] == 0:
            continue
        for j in range(i * 2, max_value+1, i):
            sosu[j] = 0

    for n in range(1,len(tmp)+1):
        for i in permutations(tmp, n):
            num = [j for j in i]
            num = int("".join(num))
            answer += sosu[num]
            sosu[num] = 0

    return answer

print(solution("011"))