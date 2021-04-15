
# https://www.acmicpc.net/problem/15683
import copy
"""
4 6
0 0 0 0 0 0
0 0 0 0 0 0
0 0 1 # # 2
0 0 0 0 0 0
"""
cctv = {
    1: [[0],[1],[2],[3]],
    2: [[0,2],[1,3]],
    3: [[0,1],[1,2],[2,3],[3,0]],
    4: [[0,1,2],[1,2,3],[2,3,0],[3,0,1]],
    5: [[0,1,2,3]]
}
def fill(x,y,dir,new_board):
    if dir == 0:
        for ny in range(y+1,M):
            if new_board[x][ny] != 0:
                break
            new_board[x][ny] = '#'
    elif dir == 1:
        for nx in range(x+1,N):
            if new_board[nx][y] != 0:
                break
            new_board[nx][y] = '#'
    elif dir == 2:
        for ny in range(0,y):
            if new_board[x][ny] != 0:
                break
            new_board[x][ny] = '#'
    else:
        for nx in range(0,x):
            if new_board[nx][y] == 0:
                break
            new_board[nx][y] = '#'
    return new_board

def dfs(cctv_locs,cnt,dirs):
    # 동 남 서 북

    # 구조
    # 1. cctv 4번 회전하면 그 상태가 다음 cctv로 전달해야함 >> 마지막에서 빈칸을 찾으면 됨

    global board, visited, answer

    # 재귀는 무조건 리턴값먼저 생각해줘야함

    if len(cctv_locs) == cnt:
        look = board.count(0)
        return min(N*M-look, answer)


    x,y = cctv_locs[0]
    if board[x][y] == 1:
        for i in range(4):



N, M = list(map(int,input().split()))
board = []
cctv_locs = []
for i in range(N):
    row = list(map(int, input().split()))
    board.append(row)
    for j in range(M):
        if board[i][j]:
            cctv_locs.append((i,j))

answer = N * M
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
visited = copy.deepcopy(board)
dfs(cctv_locs,0,0)