from collections import deque

n, l, r = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    union = [(x, y)]
    total_population = graph[x][y]
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if l <= abs(graph[x][y] - graph[nx][ny]) <= r:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    union.append((nx, ny))
                    total_population += graph[nx][ny]

    if len(union) > 1:
        avg_population = total_population // len(union)
        for i, j in union:
            graph[i][j] = avg_population

    return len(union)

result = 0

while True:
    visited = [[False] * n for _ in range(n)]
    move_occurred = False

    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                if bfs(i, j) > 1:
                    move_occurred = True

    if not move_occurred:
        break
    result += 1

print(result)