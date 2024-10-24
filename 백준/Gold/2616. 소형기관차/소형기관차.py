import sys
input = sys.stdin.readline

n = int(input())
passengers = list(map(int, input().split()))
max_train_length = int(input())

sum_passengers = [0] * (n + 1)

for i in range(1, n + 1):
    sum_passengers[i] = sum_passengers[i - 1] + passengers[i - 1]

dp = [[0] * (n + 1) for _ in range(4)]

for i in range(1, 4):
    for j in range(i * max_train_length, n + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j - max_train_length] + (sum_passengers[j] - sum_passengers[j - max_train_length]))

print(dp[3][n])
