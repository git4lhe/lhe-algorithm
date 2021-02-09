def solution(land):
    rows = len(land)
    cols = len(land[0])

    for row in range(1,rows): # col
        for col in range(0,cols):
            tmp = max([land[row-1][i] for i in range(cols) if i != col])
            land[row][col] = max(land[row][col],land[row][col] + tmp)

    return max(land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))