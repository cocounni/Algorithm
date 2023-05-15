from sys import stdin as s

s = open("input.txt", "rt")

N, M = map(int, s.readline().split())

didnt_hear = set()
didnt_see = set()
result = []

for _ in range(N):
    didnt_hear.add(s.readline().strip())

for _ in range(M):
    didnt_see.add(s.readline().strip())

# 이 아래 코드에서 for 중첩을 안 써야 시간초과 해결
# for i in didnt_hear:
#     for j in didnt_see:
#         if (i == j):
#             result += j

result = sorted(list(didnt_hear & didnt_see))

print(len(result))
for name in result:
    print(name)