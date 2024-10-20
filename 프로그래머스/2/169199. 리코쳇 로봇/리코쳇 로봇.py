from collections import deque

def solution(board):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    rows = len(board)
    cols = len(board[0])
    
    start = None
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == 'R':
                start = (r, c)
                break
        if start:
            break
    
    def bfs(start):
        queue = deque([start])
        visited = set([start])
        steps = 0
        
        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                
                if board[x][y] == 'G':
                    return steps
                
                for dx, dy in directions:
                    nx, ny = x, y
                    
                    while 0 <= nx + dx < rows and 0 <= ny + dy < cols and board[nx + dx][ny + dy] != 'D':
                        nx += dx
                        ny += dy
                    
                    if (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
            steps += 1
        
        return -1
    
    return bfs(start)
