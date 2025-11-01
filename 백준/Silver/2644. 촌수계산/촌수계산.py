from collections import deque

n = int(input())
a, b = map(int, input().split())
m = int(input())

rels = {i: [] for i in range(1, n+1)}
for _ in range(m):
    i, j = map(int, input().split())
    rels[i].append(j)
    rels[j].append(i)

visited = set()
def bfs(x):
    q = deque([(x, 0)])
    visited.add(x)

    while q:
        x, depth = q.popleft()
        if x == a:
            return depth

        for y in rels[x]:
            if not y in visited:
                q.append((y, depth+1))
                visited.add(y)
    return -1

print(bfs(b))