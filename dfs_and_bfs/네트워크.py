def dfs(n,computers,node, visited):

    if visited[node]:
        return

    visited[node] = True
    for i in range(len(computers)):
        if (not visited[i]) and (computers[node][i]):
            dfs(n,computers,i,visited)


def solution(n,computers):
    visited = [0] * n

    count = 0
    for i in range(n):
        for j in range(n):
            if (not visited[j]) and (computers[i][j] == 1):
                dfs(count,computers,j,visited)
                count += 1

    return count

print(solution(6, [[1, 0, 1, 1, 0, 0], [0, 1, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1], [1, 0, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1], [0, 1, 1, 1, 1, 1]]))