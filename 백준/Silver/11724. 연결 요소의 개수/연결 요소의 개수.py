from collections import deque

N, M = map(int, input().split())
graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

visited = set()

def bfs(u):
    q = deque([u])
    visited.add(u)

    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in visited:
                q.append(v)
                visited.add(v)

cnt = 0
for i in range(1, N + 1):
    if i not in visited:
        bfs(i)
        cnt += 1

print(cnt)
