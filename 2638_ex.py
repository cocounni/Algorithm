# https://resilient-923.tistory.com/318

from sys import stdin as s
from collections import deque

s=open("input.txt", "rt")

N, M = map(int, s.readline().split())

graph = [list(map(int, s.readline().split())) for _ in range(N)]

dx = [0, 0, -1, 1]          # 상, 하, 좌, 우
dy = [1, -1, 0, 0]
visited = []

# BFS 이용해서 1(치즈가 있을 경우) BFS 진행 X / 0일 경우 BFS 진행
# 2변 이상 접촉 확인 후 녹게 하려면 BFS 구현해서 2차원 배열 탐색 시, 배열 값이 1(치즈 있음)일 경우 값을 1씩 더해서 총 2번 더한 값이 3이 되면 녹는다고 가정

def bfs():
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < N and 0 <= ny < M and visited[nx][ny] == 0:
                if graph[nx][ny] >= 1:
                    graph[nx][ny] += 1
                else:
                    visited[nx][ny] = 1
                    q.append([nx, ny])

time = 0
while 1:
    visited = [[0]*M for _ in range(N)]
    bfs()
    flag = 0
    for i in range(N):
        for j in range(M):
            if graph[i][j] >= 3:
                graph[i][j] = 0
                flag = 1
            elif graph[i][j] == 2:
                graph[i][j] = 1
    if flag == 1:
        time += 1
    else:
        break

print(time)
# print(graph)