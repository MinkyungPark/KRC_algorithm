maps = [input().split() for _ in range(5)]
routes = set()

def dfs(x, y, route):
    if len(route) == 6:
        routes.add(''.join([maps[i][j] for i, j in route]))
        return
    
    for dx, dy in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
        nx, ny = x + dx, y + dy
        if (0 <= nx < 5) and (0 <= ny < 5):
            dfs(nx, ny, route + [(nx, ny)])

for i in range(5):
    for j in range(5):
        dfs(i, j, [(i, j)])

print(len(routes))