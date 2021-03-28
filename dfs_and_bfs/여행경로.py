# queue 문제인거같음

import copy
def dfs(v, tickets, visited,answer):
    if sum(visited) == len(tickets):
        return answer

    for n,(start,end) in enumerate(tickets):
        if v == start and not visited[n]:
            visited[n] = True
            answer.append(end)
            final = dfs(end, tickets, visited,answer)
            if final:
                return final
            visited[n]=False
            answer.pop()

def solution(tickets):
    tickets.sort()

    visited = [False] * len(tickets)
    answer = ['ICN']
    f = dfs('ICN', tickets, visited,answer)
    return f

# print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
print(solution([['ICN', 'B'], ['B', 'C'], ['C', 'ICN'], ['ICN', 'D'], ['ICN', 'E'], ['E', 'F']]))