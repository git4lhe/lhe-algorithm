from collections import deque

# 1. r,c는 1부터 시작한다
# 2. 치킨거리 abs(r1-r2) + abs(c1-c2)
# 3. 1=집, 2=치킨집, N*N MAP
# 4. N=행열, M = 치킨개수는 M보다 크거나 같음
# 5. 도시의 치킨거리 = 모든 집의 치킨거리 합

# 먼저 2의 x,y좌표를 넣는다
# x 좌표의 combination값을 구함
# result로 min(result, tmp) 비교
import copy


def get_distance(selected_stores):
    all_dis = 0
    for house in houses:
        min_distance = 987654321
        for s in selected_stores:
            d = abs(stores[s][0] - house[0]) + abs(stores[s][1] - house[1])
            min_distance = min(min_distance, d)
        # 집 한 곳마다 최소 거리 계산
        all_dis += min_distance

    return all_dis


def DFS(L, BeginWith):

    # 종료 조건
    if L == r:
        all_comb.append(copy.deepcopy(comb))
    else:
        for i in range(BeginWith, len(stores)):
            comb[L] = i
            DFS(L + 1, i + 1)


N, M = list(map(int, input().split()))
stores = []
houses = []
city = []
for i in range(N):
    row = list(map(int, input().split()))
    city.append(row)
    for j in range(N):
        if city[i][j] == 2:
            stores.append((i, j))
        elif city[i][j] == 1:
            # x,y,distance
            houses.append((i, j))

result = 987654321
comb = []
all_comb = []
for r in range(1, M + 1):
    comb = [0] * r
    DFS(0, 0)

for combs in all_comb:
    result = min(result, get_distance(combs))

print(result)
