from collections import deque

def solve():
    global x,y
    for direction in directions:
        nx, ny = x + dx[direction-1], y + dy[direction-1]

        if 0 <= nx < N and 0 <= ny < M:
            if direction == 1: # 동
                dice_y.rotate(1)
                dice_x[0], dice_x[2] = dice_y[0], dice_y[2]

            elif direction == 2: # 서
                dice_y.rotate(-1)
                dice_x[0], dice_x[2] = dice_y[0], dice_y[2]

            elif direction == 3: # 남
                dice_x.rotate(1)
                dice_y[0], dice_y[2] = dice_x[0], dice_x[2]
            else: # 북
                dice_x.rotate(-1)
                dice_y[0], dice_y[2] = dice_x[0], dice_x[2]

            if board[nx][ny] == 0:
                board[nx][ny] = dice[dice_x[2]]
            else:
                dice[dice_x[2]] = board[nx][ny]
                board[nx][ny] = 0
            x, y = nx, ny
            print(dice[dice_y[0]])

    return result

N,M, x,y, k = list(map(int,input().split()))

board = []
for i in range(N):
    board.append(list(map(int,input().split())))

directions = list(map(int, input().split()))
dice_x = deque([1,5,6,2])
dice_y = deque([1,3,6,4])
dice = [-1,0,0,0,0,0,0]

#동 서 남 북
dx = [0,0,-1,1]
dy = [1,-1,0,0]
result = solve()
#
# for i in result:
#     print(i)