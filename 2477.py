# from sys import stdin as s

# s=open("input.txt", "rt")

k = int(input())

# info = 방향과 각 변의 길이 저장
info = [list(map(int, input().split())) for _ in range(6)]

width = 0; height = 0;   # 가로변, 세로변
long_wid = 0; long_hei = 0;  

for i in range(len(info)):
    if info[i][0] == 1 or info[i][0] == 2:      # 방향값이 동, 서면 가로변
        if width < info[i][1]:
            width = info[i][1]      # for문 돌고 나면 가장 긴 가로변 저장됨
            long_wid = i

    elif info[i][0] == 3 or info[i][0] == 4:    # 방향값이 남, 북이면 가로변
        if height < info[i][1]:
            height = info[i][1]     # for문 돌고 나면 가장 긴 세로변 저장됨
            long_hei = i

subW = abs(info[(long_wid - 1) % 6][1] - info[(long_wid + 1) % 6][1])
subH = abs(info[(long_hei - 1) % 6][1] - info[(long_hei + 1) % 6][1])

result = ((width * height) - (subW * subH)) * k
print(result)