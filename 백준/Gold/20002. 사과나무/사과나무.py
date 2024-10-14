import sys
input = sys.stdin.read

data = input().splitlines()
n = int(data[0])
grid = [list(map(int, data[i+1].split())) for i in range(n)]

prefix_sum = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n+1):
    for j in range(1, n+1):
        prefix_sum[i][j] = (grid[i-1][j-1] 
                            + prefix_sum[i-1][j] 
                            + prefix_sum[i][j-1] 
                            - prefix_sum[i-1][j-1])

max_apples = -sys.maxsize

for size in range(1, n+1):
    for i in range(size, n+1):
        for j in range(size, n+1):
            total_apples = (prefix_sum[i][j] 
                            - prefix_sum[i-size][j] 
                            - prefix_sum[i][j-size] 
                            + prefix_sum[i-size][j-size])
            max_apples = max(max_apples, total_apples)

print(max_apples)