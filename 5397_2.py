import sys
T = int(sys.stdin.readline())
     # 현재 커서를 기준으로 오른쪽 배열
for _ in range(T):
    left = []       # 현재 커서를 기준으로 왼쪽 배열
    right = []
    pw = list(sys.stdin.readline().strip())
    for i in pw:
        if i == '<':
            if len(left) == 0:
                continue
            else:
                a = left.pop()
                right.append(a)
        elif i == '>':
            if len(right) == 0:
                continue
            else:
                b = right.pop()
                left.append(b)
        elif i == '-':
            if len(left) == 0:
                continue
            else:
                left.pop()
        else:
            left.append(i)
    right.reverse()
    arr = left + right
    ans = "".join(arr)
    print(ans)