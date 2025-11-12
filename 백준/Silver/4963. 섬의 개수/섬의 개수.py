from collections import deque

d = [
    (0, 0, 1, -1, 1, 1, -1, -1),
    (1, -1, 0, 0, 1, -1, 1, -1)
]

def bfs(i, j):
    global w, h, maps
    q = deque([(i, j)])
    maps[i][j] = -1
    
    while q:
        x, y = q.popleft()
        for dx, dy in zip(*d):
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < h and 0 <= ny < w
                and maps[nx][ny] != -1
            ):
                if maps[nx][ny] == 1:
                    q.append((nx, ny))
                maps[nx][ny] = -1
    return 1

w, h = map(int, input().split())
while (w, h) != (0, 0):
    maps = [list(map(int, input().split())) for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] != 1:
                maps[i][j] = -1
                continue
            cnt += bfs(i, j)
    print(cnt)
    w, h = map(int, input().split())