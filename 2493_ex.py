import sys

n = int(input())
top_list = list(map(int, sys.stdin.readline().split()))
stack = []
signal = []

for i in range(n):
    while stack:
        if stack[-1][1] > top_list[i]:
            signal.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
    
    if not stack:
        signal.append(0)
    stack.append([i, top_list[i]])

print(" ".join(map(str, signal)))