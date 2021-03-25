# import copy
def bfs(x,y,pipe):
    global result

    dx = [1,0,1]
    dy = [0,1,1]

    if (x == N-1 and y == N-1):
        result += 1
        return
g
    for i in range(3):
        # 0: 가로, 1:세로, 2:대각선
        if (i == 0 and pipe == 1) or (i == 1 and pipe == 0):
            continue

        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= N or ny >= N or maps[nx][ny] == 1:
            continue

        if i==2 and (maps[x][y+1] == 1 or maps[x+1][y] == 1):
            continue

        bfs(nx,ny,i)

result = 0
def solution():

    bfs(1,0,0)

    return result


N = int(input())
maps = [[0] * N for i in range(N)]
print(solution())
