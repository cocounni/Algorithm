import sys

t = int(sys.stdin.readline().strip())

results = []

for _ in range(t):
    n = int(sys.stdin.readline().strip())
    
    phoneNumList = []
    
    for i in range(n):
        phoneNumList.append(sys.stdin.readline().strip())
    
    phoneNumList.sort()
    
    def isConsistent(phoneNumList):
        for j in range(len(phoneNumList) - 1):
            if phoneNumList[j+1].startswith(phoneNumList[j]):
                return False
        return True
    
    # 결과 저장
    if isConsistent(phoneNumList):
        results.append("YES")
    else:
        results.append("NO")

print("\n".join(results))