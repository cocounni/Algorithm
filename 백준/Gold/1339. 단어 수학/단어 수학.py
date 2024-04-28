#from sys import stdin as s
from collections import Counter
import sys

#s = open("input.txt", "rt")

N = int(sys.stdin.readline().strip())

# alpha_weight: 알파벳별 가중치를 저장할 사전
alpha_weight = Counter()

for _ in range(N):
    arr = sys.stdin.readline().strip()
    len_arr = len(arr)
    for j, alphabet in enumerate(arr):
        # 가중치 계산 후 alpha_weight에 반영
        alpha_weight[alphabet] += 10 ** (len_arr - j - 1)

# Counter를 사용하여 가중치가 높은 순으로 정렬
occurences_list = sorted(alpha_weight.values(), reverse=True)

result_list = [number * (9-k) for k, number in enumerate(occurences_list)]

print(sum(result_list))