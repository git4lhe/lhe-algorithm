def solve(x,y,dir,answer):

     dx = [-1,0,1,0]
     dy = [0,1,0,-1]

     while(1):
        move = False
        # 0: 빈공간 1:벽 2:청소
        for i in range(4):
            dir = (dir + 3) % 4 # 반시계 방향 회전 후
            nx = x + dx[dir] # 좌표 움직임임
            ny = y + dy[dir]
            # dir = ndir # 계속 방향을 바꿔주어야함
            if room[nx][ny] == 0:
                answer += 1
                room[nx][ny] = 2
                x, y= nx,ny
                move = True
                break

        if not move:
            x = x - dx[dir] # ndir = dir 랑 똑같음 (4번회전)
            y = y - dy[dir]
            # move back
            if room[x][y] == 1: # 벽인 경우에만!!
                return answer


n, m = map(int, input().split())
x, y, d = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
# 처음 그 칸을 청소하여 1부터 시작
room[x][y] = 2
print(solve(x,y,d,1))


