import sys

N = str(int(sys.stdin.readline()))

str_list = list(N)
str_list.sort(reverse=True)

result = "".join(str_list)

print(result)