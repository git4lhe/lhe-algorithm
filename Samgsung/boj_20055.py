from collections import deque

def solve():
    t = 0
    zero_count = belt.count(0)
    while(zero_count < K):
        t += 1

        # 1. 벨트가 하나 회전한다
        belt.rotate(1)
        robot.rotate(1)

        robot[N-1] = 0

        # 2. 가장 먼저 벨트에 올라간 로봇부터 회전하는 방향으로 이동, 이동할 수 없다면 가만히 있는다
        # 로봇이 없으며, 그 칸의 내구도가 1이상 남아야함
        for i in range( N-2 , -1, -1):
            if robot[i] == 1 and robot[i+1] == 0 and belt[i+1] > 0:
                robot[i+1] = robot[i]
                robot[i] = 0
                belt[i+1] -= 1

        robot[N - 1] = 0

        # 3. 로봇 하나 올린다 (내구성이 1 이상 항상 조건 확인)
        if not robot[0] and belt[0] > 0:
            belt[0] -= 1
            robot[0] = True

        # 4. 내구도가 0인 칸의 개수가 k이상이라면 과정을 종료
        zero_count = belt.count(0)

    print(t)

    # 3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.


N, K = list(map(int, input().split()))
belt = deque(list(map(int,input().split())))
robot =  deque([False] * N)
# 내구도는 0, N

solve()