def spread_up(x,y):
    dx = [-1, -1, 0, 0, 0, 0, 1, 1, 2]
    dy = [-1, 1, -2, -1, 1, 2, -1, 1, 0]
    dv = [0.01, 0.01, 0.02, 0.07, 0.07, 0.02, 0.1, 0.1, 0.05]

    sum_value = 0
    for idx, idy, idv in zip(dx, dy, dv):
        nx = x - idx
        ny = y - idy
        sum_value += int(board[x][y] * idv)
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += int(board[x][y] * idv)

    if 0<= x-1 < N and 0<= y < N:
        board[x - 1][y] += board[x][y] - sum_value
    board[x][y] = 0

def spread_down(x,y):
    global board

    dx = [-1, -1, 0, 0, 0, 0, 1, 1, 2]
    dy = [-1, 1, -2, -1, 1, 2, -1, 1, 0]
    dv = [0.01, 0.01, 0.02, 0.07, 0.07, 0.02, 0.1, 0.1, 0.05]

    sum_value = 0
    for idx, idy, idv in zip(dx, dy, dv):
        nx = x + idx
        ny = y + idy
        sum_value += int(board[x][y] * idv)
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += int(board[x][y] * idv)

    if 0<= x+1 < N and 0<= y < N:
        board[x + 1][y] += board[x][y] - sum_value
    board[x][y] = 0

def spread_left(x,y):
    global board

    dx = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
    dy = [0, -1, 0, 1, -2, -1, 0, 1, 0]
    dv = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]

    sum_value = 0
    for idx,idy,idv in zip(dx,dy,dv):
        nx = x + idx
        ny = y + idy
        sum_value += int(board[x][y] * idv)
        if 0<=nx<N and 0<=ny<N:
            board[nx][ny] += int(board[x][y] * idv)

    if 0<= x < N and 0<= y-1 < N:
        board[x][y-1] += board[x][y] - sum_value
    board[x][y] = 0

def spread_right(x, y):
    global board

    dx = [-2, -1, -1, -1, 0, 1, 1, 1, 2]
    dy = [0, -1, 0, 1, -2, -1, 0, 1, 0]
    dv = [0.02, 0.1, 0.07, 0.01, 0.05, 0.1, 0.07, 0.01, 0.02]

    sum_value = 0
    for i,(idx, idy, idv) in enumerate(zip(dx, dy, dv)):
        nx = x - idx
        ny = y - idy
        sum_value += int(board[x][y] * idv)
        if 0 <= nx < N and 0 <= ny < N:
            board[nx][ny] += int(board[x][y] * idv)

    if 0<= x < N and 0<= y+1 < N:
        board[x][y + 1] += board[x][y] - sum_value
    board[x][y] = 0

def spread(x,y,dir):
    if dir == 0:
        spread_left(x,y)

    elif dir == 1:
        spread_down(x,y)

    elif dir == 2:
        spread_right(x,y)

    elif dir == 3:
        spread_up(x,y)

N = int(input())
board = []
org_sand = 0
for i in range(N):
    row = list(map(int,input().split()))
    board.append(row)
    org_sand += sum(row)

x,y = N // 2, N // 2

cnt = 1
dx = [0,1,0,-1]
dy = [-1,0,1,0]
# < 아래

stop = False
while(1):
    for dir in range(4):
        if dir == 2:
            cnt += 1
        for size in range(cnt):
            x = x + dx[dir]
            y = y + dy[dir]

            spread(x,y,dir)

            if x == 0 and y == 0:
                v = 0
                for i in range(N):
                    v += sum(board[i])
                print(org_sand - v)
                exit()
    cnt += 1
