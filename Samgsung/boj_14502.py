import copy
from itertools import combinations
from collections import Counter
import sys

sys.setrecursionlimit(10000)
def dfs(x,y, tmp_board):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<= nx < N and 0<= ny <M and tmp_board[nx][ny] == 0:
            tmp_board[nx][ny] = 2
            dfs(nx,ny,tmp_board)

    return tmp_board

def virus_dfs(virus_idxs,locs):
    tmp_board = copy.deepcopy(board)

    # build wall
    for loc in locs:
        if tmp_board[loc[0]][loc[1]] != 0:
            return False
        tmp_board[loc[0]][loc[1]] = 1

    # dfs
    for idx in virus_idxs:
        tmp_board = dfs(idx[0],idx[1],tmp_board)

    return tmp_board

N, M = list(map(int,input().split()))
virus_idx = []
board = [ [0] * M for _ in range(N)]
visited = [ [0] * M for _ in range(N)]

# virus idx 찾기
for i in range(N):
    row = list(map(int,input().split()))
    for j in range(M):
        board[i][j] = row[j]
        if board[i][j] == 2:
            virus_idx.append([i,j])

# 3개의 벽 찾기기
answer = 0
idx = [[i,j] for j in range(M) for i in range(N)]
for locs in combinations(idx,3):
    for virus in virus_idx:
        virus_board = virus_dfs(virus_idx,locs)
        if virus_board:
            counter = Counter(sum(virus_board,[]))
            answer = max(counter[0],answer)
print(answer)



