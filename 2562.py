n_list = []

for i in range(0, 9):
    n = int(input())
    n_list.append(n)
# 위 코드 간소화 방법 n = [input() for _ in range(9)]

print(max(n_list))
print(n_list.index(max(n_list))+1)