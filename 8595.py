# from sys import stdin as s

# s=open("input.txt", "rt")
import sys
import re

n = int(input())
word = sys.stdin.readline().split()

tmp = str(word)         # 리스트 문자열로 변환

numbers = re.findall(r'\d+', tmp)       # 문자열 내 정수 추출
# print(numbers)
real_num = list(map(int, numbers))

print(sum(real_num))