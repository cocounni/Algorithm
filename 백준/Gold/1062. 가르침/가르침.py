import sys
from itertools import combinations

#s = open("input.txt", "rt")

N, K = map(int, sys.stdin.readline().split())

essential = set("antic")
words = [set(sys.stdin.readline().strip()) - essential for _ in range(N)]

if K < 5:
    print(0)
else:
    K -= 5
    
    additional_letters = set()
    for word in words:
        additional_letters.update(word)
    
    max_readable = 0
    for comb in combinations(additional_letters, min(K, len(additional_letters))):
        learned = essential.union(comb)
        count = sum(1 for word in words if word <= learned)
        max_readable = max(max_readable, count)
    
    print(max_readable)