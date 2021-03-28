import copy
def dfs(arr,n,operation):
    if len(arr) == n:
        return None

    opers = sorted([" ","-","+"], key=lambda x: ord(x))

    for oper in opers:
        operation.append(str(oper))
        operation.append(str(arr[n]))

        if int(operation[-1]) == len(arr) and eval("".join(operation).replace(" ", "")) == 0:
            # print("".join(operation))
            answer.append(copy.deepcopy(operation))

        dfs(arr,n+1,operation)
        operation.pop()
        operation.pop()

answer = []
def solution(N):
    arr = [i for i in range(1,N+1)]
    operation = [str(arr[0])]

    dfs(arr,1,operation)
    return answer

M = int(input())
for i in range(M):
    n = int(input())
    answer = solution(n)

    print()
    answer = []


