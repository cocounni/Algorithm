import heapq

n = int(input())
lectures = [tuple(map(int, input().split())) for _ in range(n)]

lectures.sort(key=lambda x: x[1])

heap = []

for lecture in lectures:
    start, end = lecture[1], lecture[2]
    
    if heap and heap[0] <= start:
        heapq.heappop(heap)
    
    heapq.heappush(heap, end)

print(len(heap))