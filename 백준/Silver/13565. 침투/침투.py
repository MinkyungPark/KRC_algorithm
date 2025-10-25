from collections import deque

M, N = map(int, input().split())
maps = [[int(s) for s in input()] for _ in range(M)]

percolate = False

def bfs(x, y):
    global percolate
    q = deque([(x, y)])
    maps[x][y] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < M and 0 <= ny < N
                and not maps[nx][ny]
            ):
                q.append((nx, ny))
                maps[nx][ny] = 1
                if nx == (M - 1):
                    percolate = True
                    return

for j in range(N):
    if percolate:
        break
    if maps[0][j]:
        continue
    bfs(0, j)

if percolate:
    print("YES")
else:
    print("NO")