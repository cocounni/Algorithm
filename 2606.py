import sys

# c: 컴퓨터의 수 / n: 네트워크 상에서 연결되어 있는 컴퓨터 쌍의 수
c = int(input())
n = int(input())

visited = [False] * (c + 1)
count = 0       # 바이러스에 걸리게 되는 컴퓨터의 수 count
graph = [[] for _ in range(c + 1)]

for i in range(n):      # 그래프 생성
    a, b = map(int, sys.stdin.readline().split())
    graph[a] += [b]     # a에 b연결
    graph[b] += [a]     # b에 a연결 -> 양방향

# def dfs(start, depth):
    
#     visited[start] = True

#     # 시작점을 기준으로 dfs로 그래프 탐색
#     for i in graph[start]:
#         if not visited[i]:
#             dfs(i, depth + 1)


# for i in range(1, c + 1):
#     if not visited[i]:
#         if not graph[i]:
#             count += 1
#             visited[i] = True
#         else:
#             dfs(i, 0)
#             count += 1

# print(count)

def dfs(n):
    visited[n] = 1
    for nx in graph[n]:
        if visited[nx] == 0:
            dfs(nx)

dfs(1)
print(sum(visited)-1)