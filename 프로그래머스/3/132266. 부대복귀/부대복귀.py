import heapq
import sys

INF = sys.maxsize

def solution(n, roads, sources, destination):
    graph = [[] for _ in range(n + 1)]
    for u, v in roads:
        graph[u].append((v, 1))
        graph[v].append((u, 1))

    def dijkstra(start):
        dist = [INF] * (n + 1)
        dist[start] = 0
        pq = []
        heapq.heappush(pq, (0, start))

        while pq:
            current_dist, current_node = heapq.heappop(pq)

            if dist[current_node] < current_dist:
                continue

            for next_node, weight in graph[current_node]:
                next_dist = current_dist + weight
                if next_dist < dist[next_node]:
                    dist[next_node] = next_dist
                    heapq.heappush(pq, (next_dist, next_node))

        return dist

    distances = dijkstra(destination)

    answer = []
    for source in sources:
        if distances[source] == INF:
            answer.append(-1)
        else:
            answer.append(distances[source])

    return answer