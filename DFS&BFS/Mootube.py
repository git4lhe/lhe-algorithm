INF = int(1e9)

def get_smallest_node():


def dijkstra(start):
    destination = [INF] * (N+1)
    destination[start] = True








N,Q = map(int,input().split())

graph = [[] for i in range(N)]
visited = [False] * (N+1)


for _ in range(N):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

for _ in range(Q):
    a,b = map(int,input().split())
    destination = [0] * (N+1)
    dijkstra(a)
    print(destination[b])