n,m = map(int,input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

# (n,m)
# i행이 지나갈때마다 max_idx을 찾음
# i+1행에서 max_idx(board[i+1][max_idx-1:max_idx+2])
# i+1행에서 max_idx 저장

# 초기값
dp = []
dp.append(max(board[:][0]))
max_idx = board[:][0].index(board[dp[0]])
for i in range(1,m+1):
    max_val = max(board[:][max_idx-1:max_idx+2])
    max_idx = board[:][i].index(max_val)

