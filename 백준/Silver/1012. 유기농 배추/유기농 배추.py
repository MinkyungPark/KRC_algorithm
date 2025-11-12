from collections import deque

def bfs(x, y):
    q = deque([(x, y)])
    farm[x][y] = 0

    while q:
        x, y = q.popleft()
        for dx, dy in zip((0, 1, 0, -1), (1, 0, -1, 0)):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < M and 0 <= ny < N
                and farm[nx][ny] == 1
            ):
                q.append((nx, ny))
                farm[nx][ny] = 0
    return 1

T = int(input())
res = []
for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0] * N for _ in range(M)]
    for _ in range(K):
        i, j = map(int, input().split())
        farm[i][j] = 1
    
    cnt = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1:
                cnt += bfs(i, j)
    res.append(cnt)

print(*res, sep='\n')
