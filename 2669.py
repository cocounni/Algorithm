# 2669 직사각형 네개의 합집합의 면적 구하기

xy_list = []
cnt = 0

while cnt < 4:
    x1, y1, x2, y2 = list(map(int, input().split()))

    for i in range(x1, x2):
        for j in range(y1, y2):
            xy_list.append([i, j])
    
    cnt += 1

list_area = [] # 면적 저장 리스트
for k in xy_list: # 같은 값이 있는 경우 저장하지 않음
    if k not in list_area:
        list_area.append(k)

print(len(list(list_area))) # 면적의 개수 출력