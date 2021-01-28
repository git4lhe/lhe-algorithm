def solution(n):
    string = str(n)
    answer = 0
    for s in string:
        answer += int(s)

    return answer