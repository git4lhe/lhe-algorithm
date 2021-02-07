# 예산문제 비슷
from collections import deque
def solution(people, limit):
    answer = 0

    # 1. sorting
    # 2. 이중포문 사용해서
    # curr=i, limit 초과하지 않는 선에서
    # 제일 큰 무게를 가진 사람
    # 더 클 경우 그냥 혼자 탐
    people.sort(reverse=True)

    people = deque(people)
    while people:
        if people[0] + people[-1] <= limit and len(people) >= 2:
            answer += 1
            people.pop()
            people.popleft()
        else:
            people.popleft()
            answer += 1

    return answer

print(solution([70,80,50], 100))
