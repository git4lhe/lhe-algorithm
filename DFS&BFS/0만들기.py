

import copy
def dfs(arr,n):
    if len(arr) == n:
        opers.append(copy.deepcopy(arr))
        return

    arr.append(" ")
    dfs(arr,n)
    arr.pop()

    arr.append("+")
    dfs(arr,n)
    arr.pop()

    arr.append("-")
    dfs(arr,n)
    arr.pop()




test_case = int(input())
for _ in range(test_case):
    n = int(input())


    opers = []
    dfs([],n-1) # operater는 n-1(숫자 사이 간 개수)

    eq = ""
    # print(opers)
    for oper in opers:
        eq = ""
        for i in range(1,n):
            eq += str(i) + oper[i-1]
        eq += str(n)
        if eval(eq.replace(" ","")) == 0:
            print(eq)
    print()
