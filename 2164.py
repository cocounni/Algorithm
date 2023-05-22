import sys
from collections import deque

n = int(sys.stdin.readline())
dq = deque([i for i in range(1, n+1)])
\
# 짝수 / 홀수 나눠서 언제 삭제하고 언제 맨 아래로 내리는지 알고리즘 짜서 추가.
# 1. 맨 위 카드를 바닥에 버림
# 2. 그 다음 위에 있는 카드를 맨 아래로 옮김

while(len(dq) > 1):
    dq.popleft()
    move = dq.popleft()
    dq.append(move)

print(dq[0])

