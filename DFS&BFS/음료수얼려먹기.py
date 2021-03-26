def dfs(x,y,maps,N,M):

    maps[x][y] = 1

    dx = [0,0,1,-1]
    dy = [1,1,0,0]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < M and maps[nx][ny] == 0:
            maps[nx][ny] = 1
            dfs(nx,ny,maps,N,M)
import copy
def new_dfs(maps,x,y,N,M):

    if (x <= -1 or x >= N) or (y <= -1 or y >= M):
        return False
    new_map = copy.deepcopy(maps)

    if maps[x][y] == 0:
        maps[x][y] = 1
        new_dfs(maps,x-1,y,N,M)
        new_dfs(maps,x,y+1,N,M)
        new_dfs(maps,x+1,y-1,N,M)
        new_dfs(maps,x,y-1,N,M)
        return True

    # maps[x][y] ==1 일때
    return False

def solution():
    maps = [[0,0,1,1,0],
            [0,0,0,1,1],
            [1,1,1,1,1],
            [0,0,0,0,0]]

    cnt = 0
    N = len(maps)
    M = len(maps[0])

    for i in range(N):
        for j in range(M):
            if maps[i][j] == 0:
                if new_dfs(maps, i,j, N, M):
                    cnt += 1
                # dfs(i,j,maps,N,M)

    return cnt

print(solution())