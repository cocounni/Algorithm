import sys

N = int(input())
arr = input().rstrip()

arr2 = list(map(int, arr))
result = sum(arr2)
print(result)