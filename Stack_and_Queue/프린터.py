from collections import deque
def solution(priorities, location):
    # 위치에 대한 값 저장
    priorities = deque(priorities)
    loc_arr = deque([i for i in range(len(priorities))])
    answer = []

    for i in range(len(priorities)):
        max_value = max(priorities)

        while priorities:
            if priorities[0] == max_value:
                answer.append((priorities[0],loc_arr[0]))
                priorities.popleft()
                loc_arr.popleft()
                break
            front, loc  = priorities.popleft(), loc_arr.popleft()
            priorities.append(front)
            loc_arr.append(loc)

    for n,(v, loc) in enumerate(answer):
        if loc == location:
            return n+1

print(solution([1, 1, 9, 1, 1, 1],0))