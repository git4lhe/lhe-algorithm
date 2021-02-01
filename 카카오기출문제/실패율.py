def solution(N, stages):
    # 스테이지 도달했으나, 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수

    stages.sort()
    players = len(stages)
    answer = {}

    for i in range(1, N + 1):
        if players != 0:
            count = stages.count(i)
            answer[i] = count / players
            players -= count
        else:
            answer[i] = 0
    print(answer)
    return sorted(answer, key=lambda x: answer[x], reverse=True)

print(solution(5,[2, 1, 2,1, 2, 4, 1, 3]))



