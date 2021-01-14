# boj 1463
# 1로 만들기
# 정수 x가 주어졌을 때, 사용할 수 있는 연산을 토대로 값을 1로 만드는 연산 횟수 구하는 문제

# dp[i] = i가 되기위한 최소 연산 횟수임

x = int(input())
dp = [0] * (x+1) # 마지막 idx = 30000

for i in range(2,x+1):

    # 빼기만 하는 경우
    dp[i] = dp[i-1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1 ) # i -> i/2 (연산 횟수 +1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1 )

print(dp[-1])