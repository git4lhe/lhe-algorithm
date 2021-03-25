from collections import defaultdict
def solution(n, costs):
    answer = 0
    # 거리가 짧은것부터 확인함!!!!!

    costs.sort(key=lambda x:x[2])
    visited = [False] * n
    visited[0] = True # 0부터 시작한다고 가정

    while sum(visited) != n:

        for cost in costs:
            start,end,dis = cost

            # 둘 중 하나만 visited했을 때
            if visited[start] or visited[end]:

                # 둘다 visit했을 때는 skip
                if visited[start] and visited[end]:
                    continue

                # 둘 중 하나만 visit했을 때는 True
                # 바로 answer로 넘어가는 이유는
                # 이미 정렬을 했기 때문에 visit했으므로 체크안해도됨됨
                else:
                    visited[start] = True
                    visited[end]= True
                    answer += dis

                    # break문을 걸어야지, visited[i]가 업데이트가 되면서
                    # 다른 node i의 거리값을 안알아도 됨
                    # 어차피 없긴하지만,,?
                    break

    return answer

print(solution(4, [[0, 1, 1], [0, 2, 1], [1, 2, 5], [1, 3, 1], [2, 3, 8]]))