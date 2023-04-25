import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())

inDegree = [0] * (n + 1)       # 각 노드(정점)의 진입차수 저장

graph = [[] for _ in range(n + 1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)          # a다음 b가 오도록
    inDegree[b] += 1            # a -> b이므로 b의 진입차수 + 1


def topology_sort():
    queue = deque()
    result = []         # 최종 위상정렬 결과 저장

    for i in range(1, n+1):
        if inDegree[i] == 0:
            queue.append(i)

    while queue:
        current = queue.popleft()
        result.append(current)

        for i in graph[current]:
            inDegree[i] -= 1            # 나가는 간선 제거
            if inDegree[i] == 0:
                queue.append(i)

    
    for i in result:
        print(i, end=' ')

topology_sort()