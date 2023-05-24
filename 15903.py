import sys
import heapq

n, m = map(int, sys.stdin.readline().split())


card = list(map(int, sys.stdin.readline().split()))
heap = []

for i in card:
    heapq.heappush(heap, i)

for j in range(m):
    x = heapq.heappop(heap)
    y = heapq.heappop(heap)
    heapq.heappush(heap, x+y)
    heapq.heappush(heap, x+y)

print(sum(heap))



# card = list(map(int, sys.stdin.readline().split()))

# for i in card:
#     for j in range(1, m+1):
#         card.sort()             # 카드 번호 오름차순 정렬

#         # 배열 인덱스에 접근해서 특정 인덱스 값 변경
#         # index = card.index()
#         result = card[0] + card[1]

#         card[0] = result
#         card[1] = result

# print(card)