# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    dp = [-1] * (N)

    dp[0] = A[0]

    for i in range(1,N):
        start = i-6
        if start < 0:
            start = 0

        dp[i] = max(dp[start:i]) + A[i]
    # print("dp",dp,"max",max(dp[start:i]),"cur", A[i])

    return dp[-1]

print(solution([1,-2]))
print(solution([1,2,3]))
print(solution([1,-2,0,9,-1,-2]))
print(solution([1,2,3,-6,39,4,6,1]))