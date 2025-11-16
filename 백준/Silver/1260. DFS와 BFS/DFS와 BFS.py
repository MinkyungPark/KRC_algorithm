from collections import deque

N, M, V = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

for val in graph.values():
    val.sort()

def dfs():
    visited = {}
    stack = [V]

    while stack:
        u = stack.pop()
        if u not in visited:
            visited.setdefault(u)
            stack += reversed(graph[u])
    print(*list(visited.keys()))

def bfs():
    visited = [False] * (N + 1)
    q = deque([V])
    visited[V] = True
    res = []
    while q:
        u = q.popleft()
        res.append(u)
        for v in graph[u]:
            if not visited[v]:
                q.append(v)
                visited[v] = True
    print(*res)

dfs()
bfs()