N = int(input())

graph = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    i, j = map(int, input().split())
    graph[i].append(j)
    graph[j].append(i)

res = [0] * (N + 1)
stack = [1]

while stack:
    x = stack.pop()
    for y in graph[x]:
        if not res[y]:
            stack.append(y)
            res[y] = x
print(*res[2:], sep='\n')