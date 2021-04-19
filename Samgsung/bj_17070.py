def solution():

    N = int(input())
    room = [list(map(int,input().split())) for _ in range(N)]

    # dp[x][y][state]
    dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
    dp[0][1][0] = 1 # dp[0][1][0] : (0,1)에 가로로 되어있는 파이프
    # 0: 가로, 1: 세로: 2:대각선

    # range(2,N) : (0,1)부터 가로 방향으로 N까지 끌고왔을 때의 경우의 수
    for j in range(2,N):
        if not room[0][j]:
            dp[0][j][0] = dp[0][j-1][0]

    # (1,2)부터 시작하는이유: (0,1)부터 시작하고, 그 다음경우가 세로일 때는 채울 필요가 없음
    for i in range(1,N):
        for j in range(2,N):
            if not room[i][j] and not room[i][j-1] and not room[i-1][j]: # house 벽 대각선일 때
                dp[i][j][1] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]

            if not room[i][j]:
                dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][1]
                dp[i][j][2] = dp[i-1][j][1] + dp[i-1][j][2]

    print(sum(dp[N-1][N-1]))


solution()
