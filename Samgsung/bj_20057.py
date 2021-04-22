# 격자 가운데 부터 시작함
# 토네이도가 x에서 y로 이동하면, y의 모든 모래가 비율과 α가 적혀있는 칸으로 이동한다.
def spread(x, y,dir):
    # sand = board[x][y]
    locs.append([x,y,dir])
    print(locs)
    sum_up = 0
    if dir == 0: # <-, ->
        for i in range(len(left)):
            nx = x + left[i][0]
            ny = y + left[i][1]
            sum_up += int(left[i][2] * board[x][y])
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += int(left[i][2] * board[x][y])
        if 0 <= x < N and 0 <= y-1 < N:
            board[x][y-1] += (board[x][y] - sum_up)

    elif dir == 1:  # ↓



        for i in range(len(down)):
            nx = x + down[i][0]
            ny = y + down[i][1]
            sum_up += int(down[i][2] * board[x][y])
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += int(down[i][2] * board[x][y])
        if 0 <= x+1 < N and 0 <= y < N:
            board[x + 1][y] += (board[x][y] - sum_up)

    elif dir == 2: # ->
        for i in range(len(left)):
            nx = x - left[i][0]
            ny = y - left[i][1]
            sum_up += int(left[i][2] * board[x][y])
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += int(left[i][2] * board[x][y])
        if 0 <= x < N and 0 <= y+1 < N:
            board[x][y+1] += (board[x][y] - sum_up)

    elif dir == 3: # ↑
        for i in range(len(down)):
            nx = x - down[i][0]
            ny = y - down[i][1]
            sum_up += int(down[i][2] * board[x][y])
            if 0 <= nx < N and 0 <= ny < N:
                board[nx][ny] += int(down[i][2] * board[x][y])
        if 0 <= x-1 < N and 0 <= y < N:
            board[x - 1][y] += (board[x][y] - sum_up)

N = int(input())
sum_value = 0
board = []
for i in range(N):
    row = list(map(int,input().split()))
    board.append(row)
    sum_value += sum(row)


dx = [0,1,0,-1]
dy = [-1,0,1,0]
locs = []
#
left = [[0,-2, 0.05],[-1,-1,0.1],[-1,0,0.07],[-1,+1,0.01],[-2,0,0.02],
         [+1,-1,0.1],[+1,0,0.07],[+1,+1,0.01],[+2,0,0.02]]
# right = -left

down = [[-1,-1,0.01],[-1,+1,0.01], [0,+2,0.02],[0,-1,0.07],[0,-2,0.02],[0,+1,0.07],
        [+1,-1,0.1], [+1,+1,0.1],[+2,0,0.05]]
# up = -down

x, y, dir = N // 2, N // 2, 0
move = 1

while (0<=x<N and 0<=y<N):
    x = x + dx[dir % 4] * move
    y = y + dy[dir % 4] * move
    if (0<=x<N and 0<=y<N):
        spread(x,y,dir % 4)
    board[x][y] = 0

    dir += 1
    x = x + dx[dir % 4] * move
    y = y + dy[dir % 4] * move
    if (0 <= x < N and 0 <= y < N):
        spread(x,y, dir % 4)
    board[x][y] = 0

    move += 1
    dir += 1


answer = 0
for i in range(N):
    answer += sum(board[i])
print(answer)