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
            if maps[i][j]==0:
                cnt += 1
                dfs(i,j,maps,N,M)

    return cnt

print(solution())