#from sys import stdin as s
import sys
#s = open("input.txt", "rt")

N = int(sys.stdin.readline())
arr = [0 for _ in range(N)]

# 각 사람의 예상 등수 받기 / append 대신 배열 인덱스 값에 접근해서 시간 단축
for x in range(N):
    arr[x] = int(sys.stdin.readline())

arr.sort()
rank = [0 for _ in range(N)]

for r in range(N):
    rank[r] = rank[r-1] + 1

result = 0

for i, j in zip(arr, rank):
    result += abs(i - j)

print(result)