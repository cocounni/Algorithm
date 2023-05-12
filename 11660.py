from sys import stdin as s
# import sys
s = open("input.txt", "rt")

N, M = map(int, s.readline().split())

# 입력받은 값 넣을 graph
graph = [[0] * (N+1)]

for i in range(N):
    table_row = list(map(int, s.readline().split()))
    table_row.insert(0, 0)
    graph.append(table_row)

# 누적합 쌓을 dp table
dp = [[0] * (N+1) for _ in range(len(graph))]

# dp table에 누적합 쌓기
for i in range(1, len(graph)):
    for j in range(1, len(graph[1])):
        if dp[i][j-1] != 0:
            dp[i][j] = dp[i][j-1] + graph[i][j]
        else:
            dp[i][j] = graph[i][j]


for i in range(M):
    x1, y1, x2, y2 = map(int, s.readline().split())
    result = 0
    for i in range(x1, x2 + 1):
        num = dp[i][y2] - dp[i][y1 - 1]
        result = result + num
    print(result)



