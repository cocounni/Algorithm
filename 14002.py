# from sys import stdin as s
import sys

# s = open("input.txt", "rt")

size = int(sys.stdin.readline().strip())
sequence = list(map(int, sys.stdin.readline().split()))

dp = [1] * size          # [1, 1, 1, 1, 1, 1]
answer = []
# answer.append(sequence[0])     # 첫번째 값은 일단 넣어줌 (여기를 수정해야 함) -> 첫번째 값이 제일 작다는 보장이 없으므로

for i in range(size):
    for j in range(i):
        if sequence[i] > sequence[j]:               # True일 때만 i에 더하기
            dp[i] = max(dp[i], dp[j]+1)
            # answer.append(sequence[i])
print(max(dp))

max_dp = max(dp)
result = []
for i in range(size-1, -1, -1):
    if dp[i] == max_dp:
        result.append(sequence[i])
        max_dp -= 1

result.reverse()
for i in result:
    print(i, end=" ")
