from sys import stdin as s

s=open("input.txt", "rt")

N, M = map(int, s.readline().split())

arrA = list(map(int, s.readline().split()))
arrB = list(map(int, s.readline().split()))

tmp = arrA + arrB

tmp.sort()

for j in range(len(tmp)):
    print(tmp[j], end=" ")