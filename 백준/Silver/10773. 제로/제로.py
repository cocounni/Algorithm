#from sys import stdin as s

#s = open("input.txt", "rt")

import sys

K = int(sys.stdin.readline().strip())

stack = []
for _ in range(K):
    number = int(sys.stdin.readline().strip())
    if number == 0:
        stack.pop()
    else:
        stack.append(number)


print(sum(stack))