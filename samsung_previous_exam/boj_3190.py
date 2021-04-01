from collections import deque
def solve():
    t = 0
    snake_dir = 0
    snake = deque([[1,1]])

    while(1):
        if not (1<=snake[0][0]<=N and 1<=snake[0][1]<=N):
            break

        nx = snake[0][0] + dx[snake_dir]
        ny = snake[0][1] + dy[snake_dir]


        if [nx,ny] in snake:
            t += 1
            break

        else:
            # 사과가 있는지 없는지 확인하고, 위치 옮김
            # apples 사과 있을 때, 사과좌표 좌표 없애버림
            if [nx,ny] in apples:
                apples.remove([nx, ny])
            else:
            # apples 사과 없을 때, 꼬리 좌표 없애버림
                snake.pop()
            snake.appendleft([nx, ny])

        t += 1
        for dirs in direction:
            tt, d = dirs
            if t < tt:
                break

            if t == tt:
                direction.pop(0)
                if d == 'L':
                    snake_dir += 3
                else:
                    snake_dir += 1

                snake_dir %= 4
                break

        x, y = nx, ny

    print(t)

N = int(input())
k = int(input())
apples = []
for _ in range(k):
    apples.append(list(map(int,input().split())))

l = int(input())
direction = []
for _ in range(l):
    row = list(input().split())
    direction.append([int(row[0]),row[1]])


# 0:오,1:아래,2:왼,3: 위
dx = [0,1,0,-1]
dy = [1,0,-1,0]
solve()










