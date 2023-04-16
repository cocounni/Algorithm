import sys

n = int(sys.stdin.readline())
stack = []

for i in range(n):
    text = sys.stdin.readline().split()

    if text[0] == 'push':
        stack.append(text[1])
    elif text[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack.pop())
    elif text[0] == 'size':
        print(len(stack))
    elif text[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
    elif text[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)