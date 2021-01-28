from itertools import combinations

def solution(numbers):
    answer = []
    for i in combinations(numbers, 2):
        answer.append(sum(i))
    return sorted(list(set(answer)))

print(solution([5,0,2,7]))