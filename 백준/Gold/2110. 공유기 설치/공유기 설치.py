import sys
input = sys.stdin.readline

n,c=map(int,input().split())
l=[]
for i in range(n):
    tmp=int(input())
    l.append(tmp)

l.sort()

#누적차
dp=[0]
for i in range(1,n):
    dp.append(l[i]-l[0])
#print(dp)

#나올 수 있는 정답의 최대
ans=(l[-1]-l[0])//(c-1)

start=1
end=ans
while True: #ans~1까지 이분탐색 하며 반복 
    if start>end: #이분탐색 종료 조건..밑에 종료조건 있으니 필요없나? 
        break
    mid=(start+end)//2 #최대 거리

    #가능한지 탐색
    count=0 #설치한 공유기 개수
    index=1 #리스트 순회 인덱스
    최근공유기=0 #가장 최근에 설치한 공유기 인덱스
    while True: #20만번
        if count>=c-1:
            가능성=True
            break
        if index>=n:
            가능성=False
            break

        if dp[index]-dp[최근공유기]>=mid:
            count+=1
            최근공유기=index
            #print("mid:",mid, "설치!",최근공유기)
        index+=1
    #print("mid:",mid,"가능성",가능성,",count:",count)
    if 가능성==True: #형성 되는 경우를 담아놓기
        ans=mid
        start=mid+1
    else:
        end=mid-1

print(ans)