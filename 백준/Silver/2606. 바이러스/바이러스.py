from collections import deque

N = int(input())
M = int(input())

graph = {i: [] for i in range(1, N + 1)}
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)
cnt = 0
q = deque([1])
visited[1] = True
while q:
    u = q.popleft()

    for v in graph[u]:
        if not visited[v]:
            cnt += 1
            q.append(v)
            visited[v] = True

print(cnt)