import sys

n, l = map(int, sys.stdin.readline().split())
leak_p = list(map(int, sys.stdin.readline().split()))

#물이 새는 곳의 위치를 오름차순 정렬한 후 시작
leak_p.sort()

new = 0
tape_count = 0

for i in leak_p:
    if new < i:
        tape_count += 1

        new = i + l - 0.5

print(tape_count)
