a, x = map(int, input().split())
num_list = list(map(int, input().split()))

for i in range(a):
    if num_list[i] < x:
        print(num_list[i], end = " ")

# 출력값 한줄로 나오도록 추가할것
# , end=" "