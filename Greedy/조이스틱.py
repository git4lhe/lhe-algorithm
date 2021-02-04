def get_chr_count(num):
    return min(abs(ord(num)-ord('A')), abs(1+ord('Z')-ord(num)))


def solution(name):
    name = [i for i in name]
    start = ['A']* len(name)

    # default
    change = [get_chr_count(ch) for ch in name]
    idx = 0
    answer = 0

    left, right = 1, 1
    while (1):
        answer += change[idx]

        change[idx] = 0
        if sum(change) == 0:
            return answer

        left,right = 1,1
        while change[idx-left] == 0:
            left += 1
        while change[idx+right] == 0:
            right += 1

        answer += left if left < right else right
        idx += -left if left < right else right


print(solution("JAN"))