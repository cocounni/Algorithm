import sys

# 사대의 수 M, 동물의 수 N, 사정거리 L
m, n, l = map(int, input().split())
s = list(map(int, input().split()))
s.sort()


def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid+1
        else:
            right = mid - 1
    return right


count = 0
for _ in range(n):
    x, y = map(int, sys.stdin.readline().split())

    # 가장 가까운 사대의 인덱스 찾기
    idx = binary_search(s, x)

    # 가장 가까운 사대와의 거리, 오른쪽 사대와의 거리 계산하기
    dist = abs(x - s[idx]) + y
    dist_right = abs(x - s[idx+1]) + y if idx < m-1 else float('inf')

    # 가장 가까운 사대와 오른쪽 사대 중에서 최소 거리 구하기
    dist = min(dist, dist_right)

    # 동물을 잡을 수 있으면 count 증가
    if dist <= l:
        count += 1

print(count)