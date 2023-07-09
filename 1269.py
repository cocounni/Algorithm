from sys import stdin as s

s=open("input.txt", "rt")

a_cnt, b_cnt = map(int, s.readline().split())
arr_a = set(map(int, s.readline().split()))
arr_b = set(map(int, s.readline().split()))

# # print(arr_a)
print(len(arr_a-arr_b)+len(arr_b-arr_a))