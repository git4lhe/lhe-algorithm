from collections import defaultdict
def solution(clothes):
    answer = 1
    dicts = defaultdict(list)

    for i,j in clothes:
        dicts[j].append(i)

    for key,value in dicts.items():
        n = len(value)
        answer *= (n+1)

    return answer -1


ex = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
print(ex)
print(solution(ex))