'''
# 예상 : 그리디
# from bisect import bisect_left, bisect_right
# 해쉬, 그리디
출처: https://programming119.tistory.com/196 [개발자 아저씨들 힘을모아]

'''
from bisect import bisect_left, bisect_right

def solution(a):
    answer = 0
    sorted_a = sorted(a )
    rank = dict()
    rank_list = list(rank.values())
    for i, val in enumerate(sorted_a):
        rank[val] = i
    for n in a:
        rank_list.append(rank[n])

    leng = len(a)
    for i,num in enumerate(rank_list):
        j, k = i+1,leng
        cnt = 0

    return answer


def jsh_solution(a):
    answer = 2
    if 0 <= len(a) <= 2:
        return len(a)
    temp = set()
    left, right = a[0], a[-1]
    for i in range(1, len(a) - 1):
        if left > a[i]:
            temp.add(a[i])
            left = a[i]
        if right > a[-1 - i]:
            temp.add(a[-1 - i])
            right = a[-1 - i]

    return answer + len(temp)

print(jsh_solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))