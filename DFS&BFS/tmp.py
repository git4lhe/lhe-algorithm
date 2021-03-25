# # you can write to stdout for debugging purposes, e.g.
# # print("this is a debug message")
#
#
# from collections import defaultdict
#
# def solution(A):
#     # write your code in Python 3.6
#     old_dict, new_dict = defaultdict(int), defaultdict(int)
#     old_dict[A[0]] = 1
#     old_dict[-A[0]] = 1
#
#     for item in A[1:]:
#         print(item, old_dict, new_dict)
#         for i in range(-100, 101 - item):
#             new_dict[i + item] = old_dict[i]
#         for i in range(-100 + item, 101):
#             new_dict[i - item] = max(old_dict[i], new_dict[i - item])
#         old_dict, new_dict = new_dict, defaultdict(int)
#
#     # print(old_dict)
#     for i in range(0, 101):
#         if old_dict[i] == 1 or old_dict[-i] == 1:
#             return i
#
#     return 100
#
# print(solution([1, 5, 2, -2]))

# for i in range(-100, 101):
#     print(i)


from itertools import combinations
def MinAbsSum(A):
    N = len(A)
    M = 0
    for i in range(N):
        A[i] = abs(A[i])
        M = max(A[i], M)
    S = sum(A)
    count = [0] * (M + 1)
    for i in range(N):
        count[A[i]] += 1
    dp = [-1] * (S + 1)
    dp[0] = 0
    for a in range(1, M + 1):
        if count[a] > 0:
            for j in range(S):
                if dp[j] >= 0:
                    dp[j] = count[a]
                elif (j >= a and dp[j - a] > 0):
                    dp[j] = dp[j - a] - 1
    result = S
    for i in range(S // 2 + 1):
        if dp[i] >= 0:
            result = min(result, S - 2 * i)
    return result
#
print(MinAbsSum([1,2,2,2,2,4,5]))