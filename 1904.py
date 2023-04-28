from sys import stdin as s

s = open("input.txt", "rt")

n = int(s.readline())

dp = [0]*(1000001)          # 괄호 안 1000001 대신 n+1 넣으면 런타임에러 발생
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])

