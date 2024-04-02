from sys import stdin

# stdin = open("input.txt", "rt")

N = int(stdin.readline())

words = []

for _ in range(N):
    word = stdin.readline().strip()
    words.append(word)

# 중복 제거
words = list(set(words))

# 먼저 단어의 길이에 따라, 그 다음 알파벳 순으로 정렬
words.sort(key=lambda word: (len(word), word))

for word in words:
    print(word)