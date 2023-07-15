from sys import stdin as s

s=open("input.txt", "rt")

n, m = map(int, s.readline().split())
card_num = list(map(int, s.readline().split()))
# card_num.sort()             # sort를 해줘야 작은수부터 순서대로 정렬되므로 슬라이딩 윈도우 해서 찾기 가능
num_sum = sum(card_num[:3])
# print(num_sum)
result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if card_num[i] + card_num[j] + card_num[k] > m:
                continue
            else:
                result = max(result, card_num[i] + card_num[j] + card_num[k])

print(result)