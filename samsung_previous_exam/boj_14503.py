def check_xy(x,y):
    if 0<=x <N and 0<=y<M:
        return True

    return False

def redirect(x,y,dir,new_dir):
    ndir = (dir + new_dir) % 4
    nx = x + dx[ndir]
    ny = y + dy[ndir]
    return nx,ny,ndir

def dfs(x,y,dir):
    global answer
    visited[x][y] = True
    answer +=1

    # 왼쪽 방향
    # 1오,2뒤,3왼쪽
    nx,ny,ndir = redirect(x,y,dir,3) #
    if check_xy(nx,ny):
        if not visited[nx][ny] and not room[nx][ny]:
            visited[nx][ny] = True
            dfs(nx,ny,dir)
        elif visited[nx][ny] or room[nx][ny]:
                _, _, ndir = redirect(x,y,dir,2)
                dfs(x,y,ndir)

        else:
            cnt = 0
            for i in range(4):
                nx,ny,ndir = redirect(x,y,dir,i)
                if room[nx][ny] == 1 or visited[nx][ny]:
                    cnt += 1

            if cnt == 4:
                nx,ny,_ = redirect(x,y,dir,2)
                if room[nx][ny] == 1:
                    return answer
                dfs(nx,ny,dir)

    return answer



N, M = list(map(int,input().split()))
sx, sy, sdir = list(map(int,input().split()))
room = []
for i in range(N):
    row = list(map(int,input().split()))
    room.append(row)

visited = [[0] * M for _ in range(N)]
answer = 0
# 북동남서
dx =[-1,0,1,0]
dy = [0,1,0,-1]
dfs(sx,sy,sdir)
print(answer)