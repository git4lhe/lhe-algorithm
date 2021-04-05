def solve():
    for i in range(N-2,-1,-1): # 역순 출력
        if i + table[i][0] <= N:
            dp[i] = max(table[i][1] + dp[i+table[i][0]],dp[i+1])
        else:
            dp[i] = dp[i+1]  # dp[N] = 0

    return dp[0]

N = int(input())
dp = [0 for i in range(N+1)]
table = []
for i in range(N):
    time, pay= list(map(int,input().split()))
    table.append([time, pay])

print(solve() )