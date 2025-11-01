from collections import deque

N = int(input())

graph = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

res = [0] * (N + 1)
def bfs(x):
    visited = set()
    q = deque([x])
    visited.add(x)

    while q:
        x = q.popleft()
        for y in graph[x]:
            if y not in visited:
                q.append(y)
                visited.add(y)
                res[y] = x

bfs(1)
for r in res[2:]:
    print(r)