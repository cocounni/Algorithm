# 10815 숫자 카드

N = int(input())
cardNum = sorted(list(map(int, input().split())))
M = int(input())
isHave = list(map(int, input().split()))

for have in isHave:
    low, high = 0, N-1  # cards의 이진 탐색 index
    exist = False
    while low <= high:
        mid = (low + high) // 2
        if cardNum[mid] > have:  # 중간 값보다 작다면
            high = mid - 1  # 중간보다 왼쪽 한 칸 옆까지 탐색
        elif cardNum[mid] < have:  # 중간 값보다 크다면
            low = mid + 1  # 중간보다 오른쪽 한 칸 옆부터 탐색
        else:
            exist = True
            break
    print(1 if exist else 0, end=' ')