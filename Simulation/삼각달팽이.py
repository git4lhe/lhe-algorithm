from itertools import chain as chainer
def solution(n):
    #
    maps = [[0] * n for i in range(n)]
    x, y =-1,0
    number = 1
    answer = []
    for i in range(n):
        for j in range(i, n):
            # 아래로
            if i % 3 == 0:
                x += 1
            # 옆으로
            elif i % 3 == 1:
                y += 1
            # 위로
            else:
                x -= 1
                y -= 1

            maps[x][y] = number
            number += 1

    # for i in range(n):
    #     for j in range(n):
    #         if maps[i][j] == 0:
    #             break
    #         answer.append(maps[i][j])
    answer = [i for i in chainer(*maps) if i !=0]
    return answer

print(solution(4))