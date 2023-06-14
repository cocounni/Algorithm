# from sys import stdin as s
import sys
# s=open("input.txt", "rt")

N, X = map(int, sys.stdin.readline().split())
# if (not (1 <= X <= N <= 250000)):         # 입력 수 크기 제한
#     exit()
arr = list(map(int, sys.stdin.readline().split()))

x_sum = sum(arr[:X])        # X일까지의 방문자 수 누적 합
result = x_sum              # 처음 담아놓은 x_sum이 최대 합일 수 있기 때문
cnt = 1                     # 최대 방문자 수를 나타낼 수 있는 기간의 수

for i in range(X, N):
    x_sum += arr[i]         # 다음 인덱스 값 더하기
    x_sum -= arr[i-X]       # x_sum의 첫 인덱스 값 빼기

    if x_sum > result:      # x_sum이 누적합의 최대값
        result = x_sum      # result에 누적합의 최대값을 넣어줌
        cnt = 1
    elif result == sum:   # 슬라이딩 윈도우를 하면서 최대값을 발견하면 cnt에 +1을 해줌
        cnt += 1

for j in range(X, N):
    if result == x_sum:
        cnt += 1

# if result == arr[0] + arr[1]:        # 첫번째 오답 1) arr배열의 첫번째 인덱스의 값과 두번째 인덱스 값의 합이 결국 x_sum이면 처음부터 +1을 해줘야 하므로
#     cnt += 1

if result == 0:
    print("SAD")
else:
    print(result)
    print(cnt)

