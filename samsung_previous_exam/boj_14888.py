import copy

def dfs(opers,n,curr):
    if N - 1 == n:
        return result_list.append(copy.deepcopy(curr))

    oper_list = ['+','-','*','/']

    for i in range(4):
        if opers[i] > 0:
            opers[i] -= 1
            curr.append(oper_list[i])
            dfs(opers,n+1,curr)
            opers[i] += 1
            curr.pop()

N = int(input())
numbers = list(map(int,input().split()))
num_opers = list(map(int,input().split()))
result_list = []

dfs(num_opers,0,[])

minimum = 1000000001
maximum = -1000000001

for k, opers in enumerate(result_list):
    start = numbers[0]
    for i, op in enumerate(opers):
        if op == '+':
            start += numbers[i+1]
        elif op == '-':
            start -= numbers[i+1]
        elif op == '*':
            start *= numbers[i+1]
        elif op == '/':
            if start < 0:
                start *= -1
                start //= numbers[i+1]
                start *= -1
            else:
                start //= numbers[i+1]

    minimum = min(start,minimum)
    maximum = max(start,maximum)

print(maximum)
print(minimum)
