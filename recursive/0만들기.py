# 백준7490 https://www.acmicpc.net/problem/7490

import copy
def recursive(arr,n):

    if len(arr) == n:
        equations.append(copy.deepcopy(arr))
        return

    arr.append(" ")
    recursive(arr,n)
    arr.pop()

    arr.append("+")
    recursive(arr,n)
    arr.pop()

    arr.append("-")
    recursive(arr,n)
    arr.pop()

# test_case
test_case = int(input()) # 항상 데이터 타입 명시

for _ in range(test_case):
    equations = []
    n = int(input())
    recursive([],n-1)

    integers = [i for i in range(1,n+1)]

    for eq in equations:
        string = ""
        for i in range(n-1):
            string += str(integers[i]) + eq[i]
        string += str(integers[-1])

        if eval(string.replace(" ", "")) == 0:
            print(string)

    print()






