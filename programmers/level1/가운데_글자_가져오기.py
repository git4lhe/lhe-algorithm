def solution(s):
    answer = ''

    v = len(s) // 2

    if len(s) % 2 == 0:
        answer = s[v - 1:v + 1]
    else:
        answer = s[v]

    return answer