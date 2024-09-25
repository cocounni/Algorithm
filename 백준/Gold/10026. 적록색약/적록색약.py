from collections import deque

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y, color, grid, visited, n):
    queue = deque()
    queue.append((x, y))
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if grid[nx][ny] == color:
                    visited[nx][ny] = True
                    queue.append((nx, ny))

n = int(input())
grid = [list(input().strip()) for _ in range(n)]

# 적록색약이 아닌 사람의 경우
visited = [[False] * n for _ in range(n)]
normalCnt = 0

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, grid[i][j], grid, visited, n)
            normalCnt += 1

visited = [[False] * n for _ in range(n)]
colorBlindCnt = 0
colorBlindGrid = []

for row in grid:
    newRow = []
    for color in row:
        if color == 'R':  # 적록색약인 사람의 경우 (R->G 변환)
            newRow.append('G')
        else:  # R이 아니면 그대로 사용
            newRow.append(color)
    colorBlindGrid.append(newRow)

for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j, colorBlindGrid[i][j], colorBlindGrid, visited, n)
            colorBlindCnt += 1

print(normalCnt, colorBlindCnt)