import sys

pay = int(sys.stdin.readline())

money = 1000 - pay
count_coin = 0

exchange = [500, 100, 50, 10, 5, 1]

for i in exchange:
        count_coin += money // i
        money = money % i       # 앞에서 나누기 연산 한 결과의 나머지가 money가 됨

print(count_coin)