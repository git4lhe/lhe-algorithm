def dfs_right(start,move):
    if start > 4 or gears[start-1][2] == gears[start][6]:
        return

    dfs_right(start+1,move*-1)
    gears[start].rotate(move)

def dfs_left(start,move):
    # 더 이상 할 수 없는 경우
    if start < 1 or gears[start+1][6] == gears[start][2]:
        return
    dfs_left(start-1,move*-1)
    gears[start].rotate(move)

from collections import deque

gears = dict()
for i in range(1,5):
    row = input()
    gears[i] = deque(map(lambda x: int(x), list(row)))

N = int(input())
for i in range(N):
    tire_num, move = list(map(int,input().split()))

    dfs_right(tire_num+1, -1 * move)
    dfs_left(tire_num-1, -1 * move)
    gears[tire_num].rotate(move)

sum = 0
for i in range(1,5):
    sum += gears[i][0] * pow(2,i-1)

print(sum)