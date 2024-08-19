import sys

#s = open("input.txt", "rt")

N = int(sys.stdin.readline())
A_list = list(map(int, sys.stdin.readline().split()))
B_list = list(map(int, sys.stdin.readline().split()))

A_list.sort(reverse=True)       # A_list 내림차순
B_list.sort()                   # B_list 오름차순

result = list(map(lambda x, y: x*y, A_list, B_list)) 

print(sum(result))