# from sys import stdin as s
import sys

s=open("input.txt", "rt")

book = dict()
n = int(input())
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if name in book:
        book[name] += 1
    else:
        book[name] = 1
max = 0
result = dict(sorted(book.items()))
for i in result:
    if (result[i]) > max:
        max = result[i]
        max_i = i
print(max_i)