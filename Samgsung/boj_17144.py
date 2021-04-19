import copy
def move_above():
    global r,c
    row,col = vaccume_loc[0]

    # 하강
    for i in range(row-1,0,-1):
        tmp[i][0] = tmp[i-1][0]
    tmp[row][col] = -1

    # 왼쪽
    for i in range(1,c):
        tmp[0][i-1] = tmp[0][i]

    # 상승
    for i in range(row):
        tmp[i][-1] = tmp[i+1][-1]

    # 오른쪽
    for j in range(c-1,0,-1):
        tmp[row][j] = tmp[row][j-1]
    tmp[row][1] = 0

def move_below():
    row, col = vaccume_loc[1]

    global r,c
    # 상승
    for i in range(row+1,r-1):
        tmp[i][0] = tmp[i+1][0]
    tmp[row][col] = -1
    # 왼쪽
    for j in range(1,c):
        tmp[-1][j-1] = tmp[-1][j]

    # 하강
    for i in range(r-1,row,-1):
        tmp[i][-1] = tmp[i-1][-1]

    # 오른쪽
    for j in range(c-1,0,-1):
        tmp[row][j] = tmp[row][j-1]
    tmp[row][1] = 0

def sum_all(arr):
    v = 0
    for i in range(len(arr)):
        v += sum(arr[i])
    return v + 2

def spread():
    global room
    for i in range(r):
        for j in range(c):
            if room[i][j] > 0:
                dv = room[i][j] // 5
                for k in range(4):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if 0<=nx<r and 0<=ny<c:
                        if room[nx][ny] >= 0:
                            tmp[i][j] -= dv
                            tmp[nx][ny] += dv

# 동서남북
dx = [0,1,0,-1]
dy = [1,0,-1,0]
room = []
vaccume_loc = []
r,c,t = list(map(int,input().split()))
for i in range(r):
    row = list(map(int,input().split()))
    room.append(row)
    for j in range(c):
        if room[i][j] == -1:
            vaccume_loc.append([i,j])

for _ in range(t):
    tmp = copy.deepcopy(room)
    spread()
    move_above()
    move_below()
    room = copy.deepcopy(tmp)
    answer = sum_all(room)

print(answer)