def solution(N, stages):
    # 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수
    fail = []
    count_value = [0] * (N + 2)
    for i in range(1, N + 2):
        count_value[i] = stages.count(i)

        # print(count_value)
    answer = []
    for i in range(1, N + 1):
        if count_value[i] == 0:
            fail.append((i, 0))
            continue

        p = count_value[i]
        all_p = sum([count_value[j] for j in range(i, N + 2)])
        # print(i, p ,all_p)
        fail.append((i, p / all_p))
    # print(fail)
    fail = sorted(fail, key=lambda x: x[1], reverse=True)

    for i, _ in fail:
        answer.append(i)
    return answer