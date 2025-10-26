N, M, R = map(int, input().split())
g = {i: [] for i in range(1, N + 1)}

for _ in range(M):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)

for k, v in g.items():
    v.sort()

visited = [0] * (N + 1) 
cnt = 1

stack = [R]
while stack:
    u = stack.pop()
    if visited[u]:
        continue
    visited[u] = cnt
    cnt += 1

    for v in g[u]:
        if not visited[v]:
            stack.append(v)


print('\n'.join(map(str, visited[1:])))