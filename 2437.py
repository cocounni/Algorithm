from sys import stdin as s

s=open("input.txt", "rt")
# import sys

N = int(s.readline())
scale = list(map(int, s.readline().split()))

scale.sort()    # 오름차순 정렬
result = 1      # 1씩 증가하면서 측정할 수 없는 값인지 확인할 값

for i in scale:
    if result < i:
        break
    result += i
print(result)
