from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        # 하루 speed 더해줌
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        if progresses[0] >= 100:
            cnt = 0
            while progresses[0] >= 100:
                cnt += 1
                progresses.popleft()
                speeds.popleft()

                if len(progresses) == 0:
                    break

            answer.append(cnt)
    return answer