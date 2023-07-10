# https://claude-u.tistory.com/208
from sys import stdin as s

# 한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

s = open("input.txt", "rt")

N, K = map(int, s.readline().split())
stuff = [[0,0]]

# 1) x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어준다.
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):              # stuff = [(w1, v1), (w2, v2) .... ]
    stuff.append(list(map(int, s.readline().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]

        # weight보다 작으면 위의 값을 그대로 가져온다
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j]

        # 3-1, 3-2
        else:
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])


# 알고리즘
# 1) x축엔 가방 1~K 까지의 무게, y축은 물건 N개 개수 만큼의 배열을 만들어준다.

# 2) 행을 차례대로 돌며 다음과 같은 알고리즘을 수행해준다.

# 3-0) 현재 물건이 현재 돌고있는 무게보다 작다면 바로 [이전 물건][같은 무게] (knapsack[i-1][j]를 입력해준다.

# 3-1) 현재 물건을 넣어준다. 물건을 넣은 뒤의 남은 무게를 채울 수 있는 최댓값(knapsack[i-1][j-weight]을 위의 행에서 가져와 더해준다.

# 3-2) 현재 물건을 넣어주는 것보다. 다른 물건들로 채우는 값(knapsack[i-1][j])을 가져온다.

# 4) 3-1과 3-2 중 더 큰 값을 knapsack[i][j]에 저장해준다. 이 값은 현재까지의 물건들로 구성할 수 있는 가장 가치 높은 구성이다.

# 5) knapsack[N][K]는 곧, K무게일 때의 최댓값을 가리킨다.