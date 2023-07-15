import sys

n = int(sys.stdin.readline())

for i in range(1, n+1):
    num = sum(map(int, str(i)))     # sum_num = 각 자리수의 합
    sum_num = num + i
    if sum_num == n:
        print(i)
        break
    if i == n:          # 생성자가 없다는 의미
        print(0)
