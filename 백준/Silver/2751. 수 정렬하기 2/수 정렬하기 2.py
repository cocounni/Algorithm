#from sys import stdin as s
import sys

#s = open("input.txt", "rt")

N = int(sys.stdin.readline())
# print(N)

numbers = []

for i in range(N):
    number = int(sys.stdin.readline().strip())
    numbers.append(number)

numbers.sort()
for j in range(len(numbers)):
    print(numbers[j])