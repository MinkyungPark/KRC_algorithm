T = int(input())

def dfs(u):
    visited.add(u)
    if (v := graph[u]) not in visited:
        dfs(v)

for _ in range(T):
    N = int(input())
    graph = {i+1: p for i, p in enumerate(list(map(int, input().split())))}
    visited = set()
    cnt = 0
    for i in range(1, N + 1):
        if i not in visited:
            cnt += 1
            dfs(i)

    print(cnt)